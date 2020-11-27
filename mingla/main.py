import os
from datetime import datetime
import yaml
import mingla.bot as bot


def main():
    #   [daily message exists] --->  [coffee reaction exists] ---> trigger 09:15, remove coffee
    #      \                             \
    #       \                             \---- OR -- sandwich ---> trigger 12:00, remove sandwich
    #        \                                   \
    #         \                                   \--- OR -- cake ----> trigger 14:50, remove cake
    #          \--- OR ---> Generate message at 09:00!

    config = yaml.load(open("config.yml"), Loader=yaml.SafeLoader)

    if os.getenv("BOT_ENV") == "production":
        bot_env = "production"
        token = os.environ["SLACK_API_TOKEN"]
    else:
        bot_env = "development"
        token = open("TOKEN").read()

    b = bot.Bot(token, config, bot_env)
    b.init_slack()

    message = b.find_daily_reaction_message()
    if not message:
        yday = datetime.now().timetuple().tm_yday
        text = config["texts"]["pre"]
        ping = ", ".join([f"<@{x}>" for x in b.list_active_users_in_room()])
        message = b.send_message(f"VOTE {yday} - {text} - {ping}")
        b.add_reaction(message, "coffee")
        b.add_reaction(message, "sandwich")
        b.add_reaction(message, "cake")
    else:
        state_list = [
            x["name"]
            for x in b.get_reactions(message)
            if config["bot_id"] in x["users"]
        ]
        if "coffee" in state_list:
            b.remove_reaction(message, "coffee")
            b.invite_members_to_room(b.get_users_reaction(message, "coffee"))
        elif "sandwich" in state_list:
            b.remove_reaction(message, "sandwich")
            b.invite_members_to_room(b.get_users_reaction(message, "sandwich"))
        elif "cake" in state_list:
            b.remove_reaction(message, "cake")
            b.invite_members_to_room(b.get_users_reaction(message, "cake"))


if __name__ == "__main__":
    main()
