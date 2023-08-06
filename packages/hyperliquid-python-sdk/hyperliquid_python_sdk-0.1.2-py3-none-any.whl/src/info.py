from src.api import API
from src.utils.types import Interval, Json


class Info(API):
    def __init__(self):
        super().__init__()

    def user_data(self, address: str) -> Json:
        """Retrieve trading details about a user.

        POST /info

        Args:
            address (str): Onchain address in 42-character hexadecimal format;
                            e.g. 0x0000000000000000000000000000000000000000.

        Returns:
            {
              userState: UserState,
              openOrders: [FrontendOrder, ...],
              fills: [Fill, ...],
              ledgerUpdates: [LedgerUpdate, ...],
              totalPoolEquity: float string,
              agentAddress: str,
              pendingWithdrawals: [WithdrawalVoucher, ...],
              meta: Meta,
              assetCtxs: [AssetCtx, ...],
              serverTime: int,
              cumLedger: float string,
              leadingPools: [LeadingPool, ...],
              isPool: bool,
              user: str
            }

            The specific contents of these values (e.g. LeadingPool) are fleshed out
            in our Gitbook docs: https://hyperliquid.gitbook.io/hyperliquid-api-docs/
        """
        return self.post("/info", {"type": "webData", "user": address})

    def user_performance(self, address: str) -> Json:
        """Retrieve a user's trading performance.

        POST /info

        Args:
            address (str): Onchain address in 42-character hexadecimal format;
                            e.g. 0x0000000000000000000000000000000000000000.

        Returns:
            {
              day: WindowPortfolio,
              week: WindowPortfolio,
              month: WindowPortfolio
            }

            where WindowPortfolio is of type

            {
                accountValueHistory: [float, float],
                pnlHistory: [float, float],
                vlm: float string,
                totLedgerChange: float string,
                accountValueChange: PortfolioChange
            }
        """
        return self.post("/info", {"type": "portfolio", "user": address})

    def l2_book(self, coin: str) -> Json:
        """Retrieve the L2 orderbook data for a given coin.

        POST /info

        Args:
            coin (str): e.g. ETH, BTC, MATIC, ATOM

        Returns:
            {
              bids: [BookLevel, ...],
              asks: [BookLevel, ...]
            }

            where BookLevel is of type

            {
              px: str,
              sz: str,
              tot: str
            }
        """
        return self.post("/info", {"type": "l2Book", "coin": coin})

    def all_mids(self) -> Json:
        """Retrieve all mids for all actively traded coins.

        POST /info

        Returns:
            {
              ATOM: float string,
              BTC: float string,
              any other coins which are trading: float string
            }
        """
        return self.post("/info", {"type": "allMids"})

    def leaderboard(self) -> Json:
        """Retrieve the trader leaderboard.

        POST /info

        Returns:
            {
              leaderboardRows: [
                {
                  accountValue: float string,
                  ethAddress: str,
                  pastMonthVolume: float string,
                  prize: int,
                  rank: int
                },
                ...
              ]
            }
        """
        return self.post("/info", {"type": "leaderboard"})

    def user_fills(self, address: str) -> Json:
        """Retrieve a given user's fills.

        POST /info

        Args:
            address (str): Onchain address in 42-character hexadecimal format;
                            e.g. 0x0000000000000000000000000000000000000000.

        Returns:
            [
              {
                closedPnl: float string,
                coin: str,
                crossed: bool,
                dir: str,
                hash: str,
                oid: int,
                px: float string,
                side: str,
                startPosition: float string,
                sz: float string,
                time: int
              },
              ...
            ]
        """
        return self.post("/info", {"type": "userFills", "user": address})

    def user_pools(self, address: str) -> Json:
        """Retrieve pools which a given user is participating in.

        POST /info

        Args:
            address (str): Onchain address in 42-character hexadecimal format;
                            e.g. 0x0000000000000000000000000000000000000000.

        Returns:
            [
              {
                name: str,
                poolAddress: str,
                leader: str,
                description: str,
                portfolio: Portfolio,
                apr: float,
                followerState: Follower or None,
                ageInDays: int,
                leaderFraction: float,
                leaderCommission: float,
                roi: float,
                followers: [Follower, ...],
                maxDistributable: float,
                maxWithdrawable: float,
                isClosed: bool
              },
              ...
            ]

            where Follower is

            {
              user: str,
              poolEquity: float,
              pnl: float,
              allTimePnl: float,
              daysFollowing: int,
              poolEntryTime: int,
              lockupUntil: int
            }
        """
        return self.post("/info", {"type": "pools", "user": address})

    def pool_details(self, pool_address: str, user_address: str | None = None) -> Json:
        """Retrieve details about a specific pool.

        POST /info

        Args:
            pool_address (str): Onchain address in 42-character hexadecimal format;
                                e.g. 0x0000000000000000000000000000000000000000.
            user_address (str, optional): Onchain address in 42-character
                                          hexadecimal format; e.g.
                                          0x0000000000000000000000000000000000000000.

        Returns:
            {
              name: str,
              poolAddress: str,
              leader: str,
              description: str,
              portfolio: Portfolio,
              apr: float,
              followerState: Follower or None,
              ageInDays: int,
              leaderFraction: float,
              leaderCommission: float,
              roi: float,
              followers: [Follower, ...],
              maxDistributable: float,
              maxWithdrawable: float,
              isClosed: bool
            }

            where Follower is

            {
              user: str,
              poolEquity: float,
              pnl: float,
              allTimePnl: float,
              daysFollowing: int,
              poolEntryTime: int,
              lockupUntil: int
            }
        """
        if user_address is None:
            return self.post("/info", {"type": "poolDetails", "poolAddress": pool_address})
        else:
            return self.post(
                "/info",
                {
                    "type": "poolDetails",
                    "poolAddress": pool_address,
                    "user": user_address,
                },
            )

    def leading_pools(self, address: str) -> Json:
        """Retrieve pools which a given user created.

        POST /info

        Args:
            address (str): Onchain address in 42-character hexadecimal format;
                            e.g. 0x0000000000000000000000000000000000000000.

        Returns:
            [
              {
                address: str,
                name: str
              },
              ...
            ]
        """
        return self.post("/info", {"type": "leadingPools", "user": address})

    def candles(self, coin: str, interval: Interval, start_time: int, end_time: int = None) -> Json:
        """Retrieve OHLC candles.

        POST /info

        Args:
            coin (str): e.g. ETH, BTC, MATIC, ATOM
            interval (Interval): Interval enum type, 1min/15min/etc
            start_time (int): UNIX timestamp in millis for start time
            end_time (int, optional): UNIX timestamp in millis for end time

        Returns:
            [
              {
                T: int,
                o: float string,
                h: float string,
                l: float string,
                c: float string,
                i: str,
                n: int,
                s: str,
                t: int,
                v: float string
              },
              ...
            ]
        """
        if end_time is None:
            return self.post(
                "/info",
                {
                    "type": "candleSnapshot",
                    "req": {
                        "coin": coin,
                        "interval": interval.value,
                        "startTime": start_time,
                    },
                },
            )
        else:
            return self.post(
                "/info",
                {
                    "type": "candleSnapshot",
                    "req": {
                        "coin": coin,
                        "interval": interval.value,
                        "startTime": start_time,
                        "endTime": end_time,
                    },
                },
            )
