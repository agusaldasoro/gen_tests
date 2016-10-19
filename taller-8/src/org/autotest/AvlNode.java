package org.autotest;

import java.util.HashSet;
import java.util.Set;


public class AvlNode {

	public int data; 
	public int height;

	public  AvlNode left;

	public  AvlNode right;

	public String toStrings() {
		Set<AvlNode> visited = new HashSet<AvlNode>();
		visited.add(this);
		return tostring(visited);
	}

	private String tostring(Set<AvlNode> visited) {
		StringBuffer buf = new StringBuffer();
		// buf.append(" ");
		// buf.append(System.identityHashCode(this));
		buf.append(" {");
		if (left != null)
			if (visited.add(left))
				buf.append(left.tostring(visited));
			else
				buf.append("!tree");

		buf.append("" + this.tostringInfoNode() + "");
		if (right != null)
			if (visited.add(right))
				buf.append(right.tostring(visited));
			else
				buf.append("!tree");
		buf.append("} ");
		return buf.toString();
	}

	private String tostringInfoNode() {
		StringBuffer buf = new StringBuffer();
		buf.append(" (");
		buf.append("" + this.data + ",");
		buf.append("" + this.height + ",");
		return buf.toString();
	}

	public AvlNode() {}

}

