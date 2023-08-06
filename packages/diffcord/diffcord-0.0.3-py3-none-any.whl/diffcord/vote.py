from __future__ import annotations
import datetime


class UserBotVote:
    """  Represents a user vote for a bot.
    """

    def __init__(self, vote_id: str, user_id: str, bot_id: str, voted_at: str, rewarded: bool, test: bool,
                 monthly_votes: int):
        """ Initialize a UserBotVote object.
        :param: vote_id: The id of the vote
        :param: user_id: The id of the user who has voted
        :param: bot_id: The id of the bot which the user has voted for
        :param: voted_at: Time of when the user voted
        :param: rewarded: Whether the user vote has been rewarded and/or acknowledged
        :param: test: Whether this is a testing bot vote (sent as a test via bot/server api dashboard) or not
        :param: monthly_votes: The number of votes this user has given this month
        """
        self.vote_id: str = vote_id
        self.user_id: int = int(user_id)
        self.bot_id: int = int(bot_id)
        self.voted_at: datetime.datetime = datetime.datetime.fromisoformat(voted_at)
        self.rewarded: bool = rewarded
        self.test: bool = test
        self.monthly_votes: int = monthly_votes

    @property
    def votes_this_month(self) -> int:
        """ Get the number of votes this user has given this month.
        :return: The number of votes this user has given this month
        """
        return self.monthly_votes

    def __repr__(self):
        return f"<UserBotVote vote_id={self.vote_id} user_id={self.user_id} bot_id={self.bot_id} voted_at={self.voted_at} rewarded={self.rewarded} testing={self.test} votes={self.monthly_votes}>"

    def __str__(self):
        return self.__repr__()


class UserVoteInformation:
    """ Represents a user vote information.
    """

    def __init__(self, user_id: str, bot_id: str, monthly_votes: int, since_last_vote: int, until_next_vote: int):
        """ Initialize a UserVoteInformation object.
        :param: user_id: The id of the target user
        :param: bot_id: The id of the bot which the user has voted for
        :param: monthly_votes: The number of votes this user has for the given bot this month
        :param: since_last_vote: Time in seconds since the last vote
        :param: next_vote: Time in seconds till the next vote
        """
        self.user_id = user_id
        self.bot_id = bot_id
        self.monthly_votes = monthly_votes
        self.since_last_vote = since_last_vote
        self.until_next_vote = until_next_vote
        self.last_vote = datetime.datetime.now() - datetime.timedelta(seconds=since_last_vote)
        self.next_vote = datetime.datetime.now() + datetime.timedelta(seconds=until_next_vote)

    def __repr__(self):
        return f"<UserVoteInformation user_id={self.user_id} bot_id={self.bot_id} votes_this_month={self.monthly_votes} since_last_vote={self.since_last_vote} until_next_vote={self.until_next_vote}>"

    def __str__(self):
        return self.__repr__()
