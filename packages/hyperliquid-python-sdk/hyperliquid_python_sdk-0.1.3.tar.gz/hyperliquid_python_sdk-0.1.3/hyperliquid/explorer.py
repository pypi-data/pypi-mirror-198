from hyperliquid.api import API
from hyperliquid.utils.types import Json


class Explorer(API):
    def __init__(self):
        super().__init__()

    def block_details(self, height: int) -> Json:
        """Retrieve details about block.

        POST /explorer

        Args:
            height (int): The height of the block to retrieve.

        Returns:
            {
              type: "blockDetails",
              blockDetails: {
                height: int,
                blockTime: int,
                hash: str,
                proposer: str,
                numTxs: int,
                txs: [
                  {
                    time: int,
                    user: str,
                    action: {
                      type: str,
                      block: int,
                      hash: str
                      optional key(s) which depend on action type: *,
                    }
                  },
                  ...
                ]
              }
            }
        """
        return self.post("/explorer", {"type": "blockDetails", "height": height})

    def recent_block_list(self, n_blocks: int) -> Json:
        """Retrieve list of most recent n blocks.

        POST /explorer

        Args:
            n_blocks (int): How many blocks to retrieve.

        Returns:
            {
              type: "blockList",
              block_summaries: [
                {
                  height: int,
                  blockTime: int,
                  hash: str,
                  proposer: str,
                  numTxs: int
                },
                ...
              ]
            }
        """
        return self.post("/explorer", {"type": "blockList", "n_blocks": n_blocks})

    def tx_details(self, tx: str) -> Json:
        """Retrieve details about transaction.

        POST /explorer

        Args:
            tx (str): Hash of the transaction to retrieve.

        Returns:
            {
              type: "txDetails",
              tx: {
                time: int,
                user: str,
                action: {
                  type: str,
                  block: int,
                  hash: str
                  optional key(s) which depend on action type: *,
                }
              }
            }
        """
        return self.post("/explorer", {"type": "txDetails", "hash": tx})

    def user_details(self, address: str) -> Json:
        """Retrieve onchain details about a user.

        POST /explorer

        Args:
            address (str): Onchain address in 42-character hexadecimal format;
                           e.g. 0x0000000000000000000000000000000000000000.

        Returns:
            {
              type: "userDetails",
              txs: [
                {
                  time: int,
                  user: str,
                  action: {
                    type: str,
                    block: int,
                    hash: str
                    optional key(s) which depend on action type: *,
                  },
                  ...
                }
              ]
            }
        """
        return self.post("/explorer", {"type": "userDetails", "user": address})
