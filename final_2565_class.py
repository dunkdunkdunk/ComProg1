class myqueue:
    def __init__(self, qid):
        self.qid='Q'+str(qid)
        self.data=[]
    def enqueue(self, e):
        self.data.append(e)
    def dequeue(self):
        if len(self.data)<1:
            print('Cannot dequeue an empty queue')
        else:self.data.pop(0)
    def __eq__(self, q2):
        return self.data==q2.data
    def __lt__(self, q2):
        return len(self.data)<len(q2.data)
    def __str__(self):
        if len(self.data)<1:return str(self.qid)+': '+'<empty>'
        return str(self.qid)+': '+', '.join(list(map(str,self.data)))
class scheduler:
    def __init__(self, n):
        self.q=[]
        for i in range(1,n+1):
            self.q.append(myqueue(i))   
    def dispatch(self, job_id):
        sorted(self.q)[0].enqueue(job_id)
    def dequeue_complete_job(self, qid):
        self.q[qid-1].dequeue()
    def print_queues(self):
        for i in self.q:
            print(i)
cmd = input().strip().split('; ')
for c in cmd: exec(c)