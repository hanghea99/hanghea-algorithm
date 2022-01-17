const LinkedListNode = (value) => {
  this.value = value;
  this.next = null;
};

const reverseList = (head) => {
  let current = head;
  let previous = null;

  while (current) {
    let temp = current.next;
    current.next = previous;
    previous = current;
    current = temp;
  }

  return previous;
};
