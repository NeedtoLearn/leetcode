class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # Compute intervals for each letter
        interval_dict = {}
        for i, v in enumerate(S):
            if v not in interval_dict:
                interval_dict[v] = (i, i)
            else:
                s, e = interval_dict[v]
                interval_dict[v] = (min(i, s), max(i, e))
        # Sort intervals by start and end
        intervals = sorted(interval_dict.values())
        # Merge intersected intervals
        partitions = []
        cur_s, cur_e = intervals[0]
        for s, e in intervals[1:]:
            if s < cur_e:
                cur_e = max(e, cur_e)
            else:
                partitions.append(cur_e - cur_s + 1)
                cur_s, cur_e = s, e
        partitions.append(cur_e - cur_s + 1)
        return partitions

