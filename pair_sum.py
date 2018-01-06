#Array pair sum implementation

def pair_sum(arr,n):

    #Edge case
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = n - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))

    print "\n".join(map(str, list(output)))

pair_sum([1,2,3,2],4)
