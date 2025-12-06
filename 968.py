MOD = 10**9+7

# 1) compute A_n
def compute_A(n_max):
    A = [0]*(n_max+1)
    A[0] = 1
    if n_max >= 1:
        A[1] = 7
    for n in range(2, n_max+1):
        A[n] = (7*A[n-1] + (A[n-2]*A[n-2]) ) % MOD
    return A

# 2) utility: modular geometric series sum: sum_{t=0..m} r^t mod MOD
def geom_sum(r, m):
    r %= MOD
    if m < 0:
        return 0
    if r == 1:
        return (m+1) % MOD
    num = pow(r, m+1, MOD) - 1
    if num < 0: num += MOD
    den = (r - 1) % MOD
    inv = pow(den, MOD-2, MOD)
    return (num * inv) % MOD

# 3) recursive DP to compute P given the 10 constraints
#    variables are in order: a,b,c,d,e with bases u = [2,3,5,7,11]
#    constraints: dict mapping frozenset({i,j}) -> cap (nonnegative int)
from functools import lru_cache

U = [2,3,5,7,11]
pairs = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]

def make_constraints_from_tuple(Xtuple):
    # Xtuple length 10 in order of pairs list above
    cons = {}
    for (p, cap) in zip(pairs, Xtuple):
        cons[frozenset(p)] = cap
    return cons

# The recursive function receives:
#   rem = tuple of remaining variable indices (e.g. (0,1,2,3,4) initially)
#   caps = tuple of individual caps for those variables (cap_i >=0)
#   cons = mapping for pairwise caps between remaining indices
# It returns sum_{nonneg integers x_i ≤ caps and x_i + x_j ≤ cons[(i,j)]} prod U[i]^x_i modulo MOD
@lru_cache(maxsize=None)
def P_rec(rem, caps_and_cons_key):
    # caps_and_cons_key will encode caps and pairwise caps in a tuple to be hashable
    # We'll decode it inside the function.
    rem = tuple(rem)
    # decode caps & cons
    # caps_and_cons_key = (caps_tuple, pair_caps_list_in_order_of_pairs_within_rem)
    caps_tuple, pair_caps = caps_and_cons_key
    k = len(rem)
    # base cases
    if k == 0:
        return 1
    if k == 1:
        # single variable i
        i = rem[0]
        cap = caps_tuple[0]
        return geom_sum(U[i], cap) % MOD

    # choose variable with smallest cap (heuristic) to minimize branches
    # rem indexed positions 0..k-1
    min_pos = min(range(k), key=lambda idx: caps_tuple[idx])
    var_index = rem[min_pos]
    var_cap = caps_tuple[min_pos]

    # Build mapping from pair (within rem) to caps
    # pair_caps is a list in lex order of pairs of rem indices
    # We need function to compute for a fixed value t of this variable, the new caps for remaining variables:
    # For every other variable j in rem, its new cap is min(old_cap_j, constraint(var,j)-t)
    # where constraint(var,j) may not exist if original cap not given -> treat as +inf
    # So first build dict cons_map[(pos1,pos2)] = cap
    cons_map = {}
    idx_map = {rem[i]: i for i in range(k)}
    # enumerate pairs in lex order of rem positions
    pair_list = []
    for i in range(k):
        for j in range(i+1, k):
            pair_list.append( (i,j) )
    for pc, (i,j) in zip(pair_caps, pair_list):
        cons_map[(i,j)] = pc

    # Compute breakpoints for variable var_index where the caps of others change.
    # For each other variable j at position jpos, the cap after fixing t is min(caps_tuple[jpos], cons(var,jpos)-t).
    # So the break happens when cons(var,jpos)-t crosses caps_tuple[jpos], i.e., t = cons(var,jpos) - caps_tuple[jpos].
    breakpoints = set()
    # always include t = 0 and t = var_cap+1 as endpoints to build intervals [lo,hi]
    breakpoints.add(0)
    breakpoints.add(var_cap+1)
    pos_var = min_pos
    for jpos in range(k):
        if jpos == pos_var: continue
        i,j = sorted((pos_var, jpos))
        if (i,j) in cons_map:
            con = cons_map[(i,j)]
            # when t > con -> no feasible (since other cap negative) but we clip endpoints
            # only consider breakpoint t0 = con - oldcap_j
            t0 = con - caps_tuple[jpos]
            # t0 can be negative or large; include t0 and t0+1 as relevant boundaries
            breakpoints.add(max(0, t0))
            breakpoints.add(max(0, t0+1))
            # Also include con - 0 (when cons(var,jpos)-t = 0) as a possible significant point
            breakpoints.add(max(0, con))
            breakpoints.add(max(0, con+1))
    # form sorted list
    bps = sorted(breakpoints)
    total = 0
    # iterate intervals [bps[i], bps[i+1]-1] intersected with [0,var_cap]
    for idx in range(len(bps)-1):
        lo = bps[idx]
        hi = bps[idx+1]-1
        if lo>hi: continue
        if lo>var_cap: break
        if hi<0: continue
        hi = min(hi, var_cap)
        # pick representative t = lo (any t in [lo,hi] gives same pattern of min caps)
        t = lo
        # check feasibility: after fixing var = t, for every pair (var, j) we must have t + 0 ≤ cons(var,j) else no j can be >=0
        feasible = True
        new_caps = []
        for jpos in range(k):
            if jpos == pos_var: continue
            i,j = sorted((pos_var, jpos))
            oldcap_j = caps_tuple[jpos]
            if (i,j) in cons_map:
                con = cons_map[(i,j)]
                newcap = min(oldcap_j, con - t)
            else:
                newcap = oldcap_j
            if newcap < 0:
                feasible = False
                break
            new_caps.append(newcap)
        if not feasible:
            continue
        # Build new rem and new pair_caps for subproblem (without the chosen var)
        new_rem = list(rem)
        new_rem.pop(pos_var)
        # build pair_caps list in lex order for the new_rem
        new_pair_caps = []
        # To extract pair caps among new_rem positions we loop pairs
        # We'll map old pair_map indices to new positions ignoring any pair involving pos_var
        pos_map_old_to_new = {}
        newpos = 0
        for oldpos in range(k):
            if oldpos == pos_var: continue
            pos_map_old_to_new[oldpos] = newpos
            newpos += 1
        for i_old in range(k):
            if i_old == pos_var: continue
            for j_old in range(i_old+1, k):
                if j_old == pos_var: continue
                # old pair (i_old,j_old) exists in cons_map? If yes take its cap otherwise +inf (but we encode as a large number)
                cap_ij = cons_map.get((i_old,j_old), 10**18)  # big sentinel for +inf
                new_pair_caps.append(cap_ij)
        # form key for recursion: (new_caps_tuple, new_pair_caps_tuple)
        new_caps_tuple = tuple(new_caps)
        new_pair_caps_tuple = tuple(new_pair_caps)
        subkey = (new_caps_tuple, new_pair_caps_tuple)
        # compute subresult recursively
        subres = P_rec(tuple(new_rem), subkey)
        # multiplier from fixing variable var to any t in [lo,hi]: sum_{x=lo..hi} U[var]^x = U[var]^lo * geom_sum(U[var], hi-lo)
        # but careful: geom_sum as defined sums from 0..m; we can compute sum_{t=lo..hi} r^t = r^lo * sum_{s=0..(hi-lo)} r^s
        r = U[var_index] % MOD
        pow_lo = pow(r, lo, MOD)
        geom = geom_sum(r, hi-lo)
        mult = (pow_lo * geom) % MOD
        total = (total + mult * subres) % MOD
    return total % MOD

# top-level wrapper to prepare caps and pair_caps from original 10 constraints for the given rem=(0,1,2,3,4)
def compute_P_from_Xtuple(Xtuple):
    # initial rem = (0,1,2,3,4)
    rem = (0,1,2,3,4)
    # initial caps for each variable v is min of constraints including v (with others >=0)
    # i.e., cap_v = min_{j != v} X_{min(v,j),max(v,j)}
    cap_list = []
    pair_map = {}
    for (i,j), cap in zip(pairs, Xtuple):
        pair_map[(i,j)] = cap
    for v in rem:
        cs = []
        for u in rem:
            if u==v: continue
            a,b = min(u,v), max(u,v)
            cs.append(pair_map[(a,b)])
        cap_list.append(min(cs))
    # pair_caps for rem in lex order of pairs of rem positions
    pair_caps = []
    for i in range(5):
        for j in range(i+1,5):
            cap_ij = pair_map.get((i,j), 10**18)
            pair_caps.append(cap_ij)
    key = (tuple(cap_list), tuple(pair_caps))
    return P_rec(rem, key)

val = compute_P_from_Xtuple([1,2,3,4,5,6,7,8,9,10])
print(val)


# usage:
A = compute_A(1009)
sum_total = 0
for n in range(100):
    Xtuple = tuple( A[10*n + i] for i in range(10) )
    print(f"{n}: {Xtuple}")
    val = compute_P_from_Xtuple(Xtuple)
    sum_total = (sum_total + val) % MOD
print(sum_total)
