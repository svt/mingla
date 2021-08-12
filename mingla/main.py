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
            reaction_users = b.get_users_reaction(message, "coffee")
            if len(reaction_users) > 1:
                b.invite_members_to_room(reaction_users)
        elif "sandwich" in state_list:
            b.remove_reaction(message, "sandwich")
            reaction_users = b.get_users_reaction(message, "sandwich")
            if len(reaction_users) > 1:
                b.invite_members_to_room(reaction_users)
        elif "cake" in state_list:
            b.remove_reaction(message, "cake")
            reaction_users = b.get_users_reaction(message, "cake")
            if len(reaction_users) > 1:
                b.invite_members_to_room(reaction_users)


if __name__ == "__main__":
    main()
