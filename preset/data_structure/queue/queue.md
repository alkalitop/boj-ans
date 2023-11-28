## Queue (큐)

### 구조
선입선출 (FIFO)
<br/>삭제 연산이 수행되는 곳을 **front**, 삽입 연산이 수행되는 곳을 **rear** 라고 함.

### 연산
- enqueue(item): rear에서 요소 삽입
- dequeue(): front의 요소 삭제
- peek(): front의 요소 반환
- size(): 큐 사이즈 반환

### 구현
- [Python의 queue - Queue로 구현](./queue.py)
- [Python의 collections - deque로 구현](./queue-col.py)
