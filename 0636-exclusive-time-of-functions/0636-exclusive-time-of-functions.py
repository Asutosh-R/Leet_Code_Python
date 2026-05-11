class Solution(object):
    def exclusiveTime(self, n, logs):

        ans = [0] * n
        stack = []

        prevTime = 0

        for log in logs:

            fn, typ, time = log.split(':')

            fn = int(fn)
            time = int(time)

            # start of a function
            if typ == "start":

                # current running function gets time till now
                if stack:
                    ans[stack[-1]] += time - prevTime

                stack.append(fn)
                prevTime = time

            # end of a function
            else:

                # current function runs inclusively
                ans[stack[-1]] += time - prevTime + 1

                stack.pop()

                # next execution starts after current time
                prevTime = time + 1

        return ans

            
            

        