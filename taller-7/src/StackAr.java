import java.util.*;

public class StackAr {

	private final static int DEFAULT_CAPACITY = 10;

	private final ArrayList<Object[]> list;
	
	private int readIndex = -1;
	
	public StackAr() {
		this(DEFAULT_CAPACITY);
	}

	public StackAr(int capacity) throws IllegalArgumentException {
		if (capacity < 0) {
			throw new IllegalArgumentException();
		}
		this.list = new ArrayList<Object[]>();
		Object[] elems = new Object[capacity];
		this.list.add(elems);
	}

	public int size() {
		return readIndex+1;
	}

	public boolean isEmpty() {
		return size() == 0;
	}

	public boolean isFull() {
		int count = 0;
		Iterator<Object[]> itr = list.iterator();
	    while (itr.hasNext()) {
	      Object[] element = itr.next();
	      count += element.length;
	    }	
		return size() == count;
	}

	public void push(Object o) throws IllegalStateException {
		if (isFull()) {
			throw new IllegalStateException();
		}
		this.readIndex++;
		int count = this.readIndex;
		Iterator<Object[]> itr = list.iterator();
	    while (itr.hasNext()) {
	      Object[] element = itr.next();
	      if (count >= element.length){
	    	  count -= element.length;
	      }else {
	    	  element[count] = o;
	    	  break;
	      }
	    }		
	}

	public void increaseCapacity(int n) throws IllegalArgumentException {
		if (n<=0) {
			throw new IllegalArgumentException();
		}
		Object[] elems = new Object[n];
		this.list.add(elems);
	}
	
	public Object pop() throws IllegalStateException {
		if (isEmpty()) {
			throw new IllegalStateException();
		}
		Object rv = this.top();
		int count = this.readIndex;
		Iterator<Object[]> itr = list.iterator();
	    while (itr.hasNext()) {
	      Object[] element = itr.next();
	      if (count >= element.length){
	    	  count -= element.length;
	      }else {
	    	  element[count] = null;
	    	  break;
	      }
	    }			
		this.readIndex--;
		return rv;
	}

	public Object top() throws IllegalStateException {
		if (isEmpty()) {
			throw new IllegalStateException();
		}
		Object rv = null;
		int count = this.readIndex;
		Iterator<Object[]> itr = list.iterator();
	    while (itr.hasNext()) {
	      Object[] element = itr.next();
	      if (count >= element.length){
	    	  count -= element.length;
	      }else {
	    	  rv = element[count];
	    	  break;
	      }
	    }			
		return rv;
	}


	@Override
	public String toString() {
		StringBuffer b = new StringBuffer();
		b.append("[");
		int i = 0;
		while (i<=readIndex) {
			if (i > 0) {
				b.append(",");
			}
			Object o = list.get(0)[i];
			String s = String.valueOf(o);
			b.append(s);
			i++;
		}
		b.append("]");
		return b.toString();
	}
}
