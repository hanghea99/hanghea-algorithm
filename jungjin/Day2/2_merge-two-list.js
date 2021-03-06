ListNode.prototype.add = (node, val) => {
  let curr;
  if (node.val === undefined) {
    node.val = val;
  } else {
    curr = node;
    while (curr.next) {
      curr = curr.next;
    }
    curr.next = new ListNode(val);
  }
};

const mergeTwoLists = (l1, l2) => {
  // 빈 리스트가 있다면 합칠 필요가 없다.
  if (!l1) return l2;
  if (!l2) return l1;
  // 둘중에 더 작은값을 추가해 새 배열을 만든다.

  let result = new ListNode();
  result.val = undefined; // 생성시 첫 val을 0이 들어가므로 첫 값을 초기화해준다.

  let nl1 = l1;
  let nl2 = l2;

  // l1, l2 중 한쪽이라도 값이 남아있는동안 계속 반복
  while (nl1 || nl2) {
    // 한쪽만 값이 남아있는 경우
    if (!nl1) {
      while (nl2) {
        result.add(result, nl2.val);
        nl2 = nl2.next;
      }
      console.log('finish', result);
      return result;
    }
    if (!nl2) {
      while (nl1) {
        result.add(result, nl1.val);
        nl1 = nl1.next;
      }
      console.log('finish', result);
      return result;
    }

    // 더 작은 값을 result에 추가 한다.
    if (nl1.val < nl2.val) {
      result.add(result, nl1.val);
      nl1 = nl1.next;
    } else {
      result.add(result, nl2.val);
      nl2 = nl2.next;
    }
    console.log(nl1, nl2, result);
  }
  return result;
};
