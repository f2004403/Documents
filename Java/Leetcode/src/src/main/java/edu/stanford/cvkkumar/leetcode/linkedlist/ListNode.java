package edu.stanford.cvkkumar.leetcode.linkedlist;

/**
 * 
 * @author cvk
 *
 */
public class ListNode {
	
	
	/**
	 * 
	 */
	private int val;
	
	/**
	 * 
	 */
	private ListNode next;
	
	/**
	 * 
	 * @param x input
	 */
	protected ListNode(final int x) {
		val = x;
		next = null;
	}
	
	/**
	 * 
	 * @param head head of the list
	 * @return string
	 */
	public static String display(ListNode head) {
		ListNode x = head; 
		StringBuffer sb = new StringBuffer();
		while (x != null) {
			sb.append(x.val + "->");
			x = x.next;
		}
		return sb.toString();
	}
}
