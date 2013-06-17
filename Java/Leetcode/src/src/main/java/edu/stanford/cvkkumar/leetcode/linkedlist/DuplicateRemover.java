package edu.stanford.cvkkumar.leetcode.linkedlist;

/**
 * 
 * @author cvk
 *
 */
public final class DuplicateRemover {
	
	/**
	 * 
	 */
	private DuplicateRemover() {
		
	}
	/**
	 * 
	 * @param head
	 * @return ListNode
	 */
	public static ListNode deleteDuplicates(ListNode head){
        
		// head is null
		if ((head == null) || (head.next == null)) {
            return head;
        }
        
        for (ListNode currentNode = head; currentNode != null; 
        		currentNode = currentNode.next) {
        	ListNode nextDistinctNode = currentNode.next;
            while ((nextDistinctNode != null) 
            		&& (nextDistinctNode.val == currentNode.val)) {
                nextDistinctNode = nextDistinctNode.next;
            }
            currentNode.next = nextDistinctNode;	
        }
        return head;
    }
	
	
	/**
	 * 
	 * @param args arguments
	 */
	public static void main(final String[] args) {
		
		ListNode head = new ListNode(1);
		head.next = new ListNode(2);
		head.next.next = new ListNode(2);
		head.next.next.next = new ListNode(3);
		System.out.println(ListNode.display(head));
		System.out.println(ListNode.display(
				DuplicateRemover.deleteDuplicates(head)));
	}
}
