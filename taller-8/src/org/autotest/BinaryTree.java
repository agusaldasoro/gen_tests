package org.autotest;

import korat.finitization.*;
import korat.finitization.impl.*;
import java.util.*;

public class BinaryTree implements korat.testing.ITestCaseListener {
    public static class Node {
        Node left;
        Node right;
    }
    private Node root;
    private int size;

    public boolean repOK() {
        if (root == null)
            return size == 0;
        // checks that tree has no cycle
        Set visited = new HashSet();
        visited.add(root);
        LinkedList workList = new LinkedList();
        workList.add(root);
        while (!workList.isEmpty()) {
            Node current = (Node) workList.removeFirst();
            if (current.left != null) {
                if (!visited.add(current.left))
                    return false;
                workList.add(current.left);
            }
            if (current.right != null) {
                if (!visited.add(current.right))
                    return false;
                workList.add(current.right);
            }
        }
        // checks that size is consistent
        return (visited.size() == size);
    }

    public static IFinitization finBinaryTree(int nodesNum, int minSize, 
            int maxSize) {
        IFinitization f = FinitizationFactory.create(BinaryTree.class);
        IObjSet nodes = f.createObjSet(Node.class, nodesNum, true);
        f.set("root", nodes);
        f.set("Node.left", nodes);
        f.set("Node.right", nodes);
        IIntSet sizes = f.createIntSet(minSize, maxSize);
        f.set("size", sizes);
        return f;
    }

    public void notifyNewTestCase(Object o) {

    }

    public void notifyTestFinished(long numOfExplored, long numOfGenerated) {}

}
