const ListNode = (val, next) => {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
};

const oddEvenList = (head) => {
  // Handle base cases
  if (!head) return head;

  // Set two pointers
  let odd = head;
  let even = head.next;
  let even_head = head.next;

  while (even && even.next) {
    odd.next = odd.next.next;
    odd = odd.next;
    even.next = even.next.next;
    even = even.next;
  }
  odd.next = even_head;
  return head;
};
