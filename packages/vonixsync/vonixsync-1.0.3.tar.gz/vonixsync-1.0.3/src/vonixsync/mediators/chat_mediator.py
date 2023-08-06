import warnings
from sqlalchemy.exc import OperationalError, IntegrityError
from ..utils import (
    fxn,
    ConnectionDatabaseError,
    print_finalized,
    NullPages,
    ApiKeyError,
)


async def sync_chat(request, repository_dict, query_timestamp):
    if "chat" not in repository_dict:
        return

    timestamp = repository_dict["chat"].select_date(query_timestamp)

    error_array = []
    try:
        pages = await request.async_summary_meta_request(timestamp)
        if pages == 0:
            raise NullPages("chat")

    except NullPages as error:
        print(SystemExit(f"\n{str(error)}"))
        return error_array.append({type(error): "No new data found from api Request"})

    last_page = pages + 1
    try:
        for page in range(1, last_page):
            data_array = await request.async_summary_data_request(timestamp, page)
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    fxn()
                    for chat in data_array:
                        try:
                            repository_dict["chat"].insert(
                                chat["id"],
                                chat["agentId"],
                                chat["queueId"],
                                chat["source"],
                                chat["sourceId"],
                                chat["name"],
                                chat["direction"],
                                chat["status"],
                                chat["holdSecs"],
                                chat["talkSecs"],
                                chat["chatSecs"],
                                chat["createdAt"],
                                chat["answeredAt"],
                                chat["finishedAt"],
                            )
                        except KeyError as error:
                            error_array.append(
                                {type(error): ApiKeyError(error, "message", chat["id"])}
                            )

                        chat_message_declared_by_user = (
                            "chat_message" in repository_dict
                        )

                        if chat_message_declared_by_user:
                            chat_message_array = chat["chatMessages"]
                            chat_message_array_length = len(chat_message_array)

                            if chat_message_array_length > 0:
                                for message in chat_message_array:
                                    try:
                                        repository_dict["chat_message"].insert(
                                            message["chatId"],
                                            message["id"],
                                            message["message"],
                                            message["direction"],
                                            message["createdAt"],
                                            message["deliveredAt"],
                                            message["readedAt"],
                                            message["answeredAt"],
                                            message["type"],
                                        )
                                    except KeyError as error:
                                        error_array.append(
                                            {
                                                type(error): ApiKeyError(
                                                    error,
                                                    "chat_message",
                                                    profiler["id"],
                                                )
                                            }
                                        )

                        profilers_declared_by_user = "profilers" in repository_dict

                        if profilers_declared_by_user:
                            profiler_array = chat["profilers"]
                            profiler_array_length = len(profiler_array)

                            if profiler_array_length > 0:
                                for profiler in profiler_array:
                                    try:
                                        repository_dict["profilers"].insert(
                                            profiler["id"],
                                            "0",
                                            profiler["chatId"],
                                            profiler["createdAt"],
                                            profiler["name"],
                                            profiler["value"],
                                        )
                                    except KeyError as error:
                                        error_array.append(
                                            {
                                                type(error): ApiKeyError(
                                                    error, "profiler", profiler["id"]
                                                )
                                            }
                                        )

                        tree_declared_by_user = "trees" in repository_dict

                        if tree_declared_by_user:
                            tree_array = chat["trees"]
                            tree_array_length = len(tree_array)

                            if tree_array_length > 0:
                                for tree in tree_array:
                                    try:
                                        repository_dict["trees"].insert(
                                            tree["id"],
                                            "0",
                                            tree["chatId"],
                                            chat["createdAt"],
                                            tree["label"],
                                        )
                                    except KeyError as error:
                                        error_array.append(
                                            {
                                                type(error): ApiKeyError(
                                                    error, "tree", tree["id"]
                                                )
                                            }
                                        )

            except IntegrityError as error:
                error_array.append({type(error): str(error.__dict__["orig"])})

    except OperationalError as error:
        error_array.append({"Database_connection_error": str(error.__dict__["orig"])})
        raise SystemExit(
            ConnectionDatabaseError(error_array).print_finalized()
        ) from error

    else:
        print_finalized(error_array, "the chat summary list")
        if chat_message_declared_by_user:
            print_finalized(error_array, "the chat messages")
        if profilers_declared_by_user:
            print_finalized(error_array, "the profilers")
        if tree_declared_by_user:
            print_finalized(error_array, "the trees")
