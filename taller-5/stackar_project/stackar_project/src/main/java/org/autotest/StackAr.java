package org.autotest;

import java.util.Arrays;

public class StackAr {

	private final static int DEFAULT_CAPACITY = 10;

	private final Object[] elems;

	private int readIndex = -1;

	public StackAr() {
		this(DEFAULT_CAPACITY);
	}

	public StackAr(int capacity) throws IllegalArgumentException {
		if (capacity < 0) {
			throw new IllegalArgumentException();
		}
		this.elems = new Object[capacity];
	}

	public int size() {
		return readIndex+1;
	}

	public boolean isEmpty() {
		return size() == 0;
	}

	public boolean isFull() {
		return size() == elems.length;
	}

	public void push(Object o) throws IllegalStateException {
		if (isFull()) {
			throw new IllegalStateException();
		}
		this.readIndex++;
		this.elems[readIndex] = o;
	}

	public Object pop() throws IllegalStateException {
		if (isEmpty()) {
			throw new IllegalStateException();
		}
		Object rv = this.top();
		this.elems[readIndex] = null;
		readIndex--;
		return rv;
	}

	public Object top() throws IllegalStateException {
		if (isEmpty()) {
			throw new IllegalStateException();
		}
		Object rv = this.elems[readIndex];
		return rv;
	}


	@Override
	public String toString() {
		StringBuffer b = new StringBuffer();
		b.append("[");
		toStringCicle(b);
		b.append("]");
		return b.toString();
	}

	private void toStringCicle(StringBuffer b){
		int i = 0;
		while (i<=readIndex) {
			if (i > 0) {
				b.append(",");
			}
			Object o = elems[i];
			String s = String.valueOf(o);
			b.append(s);
			i++;
		}
	}
}
