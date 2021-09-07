from server import Server

class Tracker:
    def __init__(self, server_instance):
        self.server = server
        self.torrent_info_hash = self._get_torrent_info_hash()

    def _get_torrent_info_hash(self):
        """
        TODO: creates the torrent info hash (SHA1) from the info section in the torrent file
        :return:
        """
        return 0 # returns the info hash

    def add_peer_to_swarm(self, peer_id, peer_ip, peer_port):
        """
        TODO: when a peers connects to the network adds this peer
              to the list of peers connected
        :param peer_id:
        :param peer_ip:
        :param peer_port:
        :return:
        """
        pass # your code here

    def remove_peer_from_swarm(self, peer_id):
        """
        TODO: removes a peer from the swarm when it disconnects from the network
              Note: this method needs to handle exceptions when the peer disconnected abruptly without
              notifying the network (i.e internet connection dropped...)
        :param peer_id:
        :return:
        """
        pass # your code here

    def broadcast(self):
        """
        TODO: broadcast the list of connected peers to all the peers in the network.
        :return:
        """
        pass # your code here

    def set_total_uploaded(self, peer_id):
        """
        TODO: sets the total data uploaded so far by the peer passed as a parameter
        :param peer_id:
        :return: VOID
        """
        pass # your code here

    def total_downloaded(self, peer_id):
        """
        TODO: sets the total data downloaded so far by the peer passed as a parameter
        :param peer_id:
        :return: VOID
        """
        pass # your code here

    def validate_torrent_info_hash(self, peer_torrent_info_hash):
        """
        TODO: compare the info_hash generated by this peer with another info_hash sent by another peer
              this is done to make sure that both peers agree to share the same file.
        :param peer_torrent_info_hash: the info_hash from the info section of the torrent sent by other peer
        :return: True if the info_hashes are equal. Otherwise, returns false.
        """
        return 0
