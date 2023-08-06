"""Cluster stacked vectors.

Designed for divisive clustering, so start with one cluster and divide until some
quality conditions are met.

Will also merge clusters. This is not an inverse of cluster division, so four
divisions then one merge will not result in three divisions. Could be used for
agglomerative clustering all the way up, but is here mostly for tie breaking when the
largest cluster is sought.

I've included some optimizations to make this workable with image colors, but dealing
with very small sets was a priority.

:author: Shay Hill
:created: 2022-09-14
"""

from __future__ import annotations

from copy import deepcopy

from cluster_colors.clusters import Cluster, Clusters

_MAX_ITERATIONS = 1000


class KMediansClusters(Clusters):
    """Clusters for kmedians clustering."""

    def converge(self) -> None:
        """Reassign members until no changes occur."""
        iterations = 0
        # if any(x.queue_add for x in self.clusters):
        while self._maybe_reassign_members() and iterations < _MAX_ITERATIONS:
            self.process_queues()
            iterations += 1

    def split_above_sse(self, max_sse: float):
        """Split while the maximum SSE is above the threshold.

        :param max_sse: the SSE threshold for splitting
        """
        while self._maybe_split_cluster(max_sse):
            self.converge()

    def split_to_count(self, count: int):
        """Split clusters until len(clusters) == count.

        :param count: the target number of clusters
        """
        while self._maybe_split_cluster() and len(self) < count:
            self.converge()

    def split_to_delta_e(self, min_delta_e: float):
        """Split clusters while no two exemplars closer than min_delta_e.

        :param min_delta_e: the minimum delta_a distance between exemplars

        It is difficult to know when to stop splitting, so this method splits one
        time too many then un-splits the last split.
        """
        prev_state: set[Cluster] | None = None
        while self.spans.valmin() > min_delta_e:
            prev_state = set(self.clusters)
            if self._maybe_split_cluster():
                self.converge()
            else:
                break
        if prev_state is not None and self.spans.valmin() < min_delta_e:
            self.sync(prev_state)

    def merge_to_find_winner(self) -> None:
        """Merge clusters until there is a clear winner."""
        while not self._has_clear_winner and self._maybe_merge_cluster():
            self.converge()

    def pop_winner(self) -> Cluster:
        """Pop the winner cluster and return it.

        :return: the largest cluster by weight
        """
        self.merge_to_find_winner()
        winner = max(self.clusters, key=lambda c: c.w)
        self.clusters.remove(winner)
        return winner

    def get_rsorted_clusters(self) -> list[Cluster]:
        """Return clusters from largest to smallest, breaking ties.

        :return: a reverse-sorted (by weight) list of clusters

        This may not return the same clusters as the iterator, because the iterator
        will not break ties. Tie-breaking will rarely be needed, but this method
        makes sure things are 100% deterministic and non-arbitrary.

        After popping all winners, the clusters will propably be sorted by weight,
        but tie breaking might have combined smaller clusters into larger clusters
        than previous winners.
        """
        clusters: list[Cluster] = []
        sacrificial_copy = deepcopy(self)
        while sacrificial_copy.clusters:
            clusters.append(sacrificial_copy.pop_winner())
        return sorted(clusters, key=lambda c: c.w, reverse=True)

    def get_rsorted_exemplars(self) -> list[tuple[float, ...]]:
        """Return clusters from largest to smallest, breaking ties.

        :return: a reverse-sorted (by weight) list of clusters

        This may not return the same clusters as the iterator, because the iterator
        will not break ties. Tie-breaking will rarely be needed, but this method
        makes sure things are 100% deterministic and non-arbitrary.

        After popping all winners, the clusters will propably be sorted by weight,
        but tie breaking might have combined smaller clusters into larger clusters
        than previous winners.
        """
        return [x.exemplar for x in self.get_rsorted_clusters()]
