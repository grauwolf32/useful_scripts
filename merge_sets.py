def merge_sets(tobe_merged,n_tresh):
    n = len(tobe_merged)
    curr_iter = tobe_merged
    next_iter = []
    curr_iter_merged = set()
    
    for iteration in xrange(0,n):
        is_ok = 0
        i = j = 0
        for i in xrange(0,len(curr_iter)):
            for j in xrange(i+1,len(curr_iter)):
                tmp_set = curr_iter[i].intersection(curr_iter[j])
                if len(tmp_set) >= n_tresh:
                    next_iter.append(curr_iter[i].union(curr_iter[j]))
                    curr_iter_merged.add(i)
                    curr_iter_merged.add(j)
                    is_ok = 1
                    break
            if is_ok == 1:
                break
            
        if is_ok != 1:
            return curr_iter
    
        p = 0
        for t in xrange(0,len(curr_iter)):
            if t not in curr_iter_merged:
                was_merged = 0
                for k in xrange(0,p+1):
                    tmp_intersect = next_iter[k].intersection(curr_iter[t])
                    if len(tmp_intersect) >= n_tresh:
                        next_iter[k] = next_iter[k].union(curr_iter[t])
                        curr_iter_merged.add(t)
                        was_merged = 1
                if was_merged == 0:
                    next_iter.append(curr_iter[t])
                    p += 1
        
        curr_iter = next_iter
        next_iter = []
        curr_iter_merged = set()        
