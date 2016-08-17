package org.autotest;

import static org.junit.Assert.*;

import org.junit.Test;

public class TestStackAr {

	@Test
	public void test() {
		StackAr a = new StackAr();
	}

	@Test (expected = IllegalArgumentException.class)
	public void failureTest() {
		StackAr a = new StackAr(-1);
	}

	
	@Test
	public void sizeTest() {
		StackAr a = new StackAr();
		a.size();
	}

	@Test
	public void isEmptyTest() {
		StackAr a = new StackAr();
		assertTrue("El Stack deberìa estar vacìo.", a.isEmpty());
	}	
	
	@Test
	public void isNotEmptyTest() {
		StackAr a = new StackAr();
		Object o = new Object();
		a.push(o);
		assertFalse("El Stack deberìa estar vacìo.", a.isEmpty());
	}	

	@Test
	public void isFullTest() {
		StackAr a = new StackAr(0);
		assertTrue("El Stack deberìa estar lleno.", a.isFull());
	}	
	
	@Test
	public void isNotFullTest() {
		StackAr a = new StackAr();
		assertFalse("El Stack no deberìa estar lleno.", a.isFull());
	}

	@Test
	public void ableToPush() {		
		StackAr a = new StackAr();
		Object o = new Object();
		a.push(o);
	}

	@Test (expected = IllegalStateException.class)
	public void cantPush() {		
		StackAr a = new StackAr(0);
		Object o = new Object();
		a.push(o);
	}

	@Test
	public void ableToPop() {
		StackAr a = new StackAr();
		Object o = new Object();
		a.push(o);
		Object o2 = a.pop();
		assertEquals(o, o2);
	}

	@Test (expected = IllegalStateException.class)
	public void cantPop() {		
		StackAr a = new StackAr();
		a.pop();
	}

	@Test
	public void ableToTop() {
		StackAr a = new StackAr();
		Object o = new Object();
		a.push(o);
		Object o1 = new Object();
		a.push(o1);
		Object o2 = a.top();
		assertEquals(o1, o2);
	}

	@Test (expected = IllegalStateException.class)
	public void cantTop() {		
		StackAr a = new StackAr();
		a.top();
	}

	@Test
	public void returnsCorrectHash(){
		StackAr a = new StackAr();
		a.push(3);
		a.push(5);
		a.push(11);

		float[] arr = new float[3];
		arr[0] = 3;
		arr[1] = 5;
		arr[2] = 11;
		int hashArr = arr.hashCode();
		int readI = 2;
		int expected = 31*(31+hashArr)+readI;

		assertEquals(expected, a.hashCode());
	}

	@Test
	public void isEqualTest(){
		StackAr a = new StackAr();
		assertTrue("Deberìan ser iguales", a.equals(a));
	}

	@Test
	public void isNullEqualTest(){
		StackAr a = new StackAr();
		StackAr b = null;
		assertFalse("No deberìa ser null a", a.equals(b));
	}

	@Test
	public void differentClassEqualTest(){
		StackAr a = new StackAr();
		int b = 3;
		assertFalse("Deberìan ser de diferente clase", a.equals(b));
	}

	@Test
	public void sameClassEqualTest(){
		StackAr a = new StackAr();
		StackAr b = new StackAr();
		b.push(2);
		assertFalse("Deberìan tener diferentes elementos", a.equals(b));
	}

	@Test
	public void sameClassAndElemsEqualTest(){
		StackAr a = new StackAr();
		StackAr b = new StackAr();
		a.push(2);
		b.push(2);
		assertTrue("Deberìan tener diferentes elementos", a.equals(b));
	}


	@Test
	public void sameClassAndElemsDiEqualTest(){
		StackAr a = new StackAr();
		StackAr b = new StackAr();
		a.push(2);
		b.push(2);
		b.pop();
		assertFalse("Deberìan tener diferentes elementos", a.equals(b));
	}

	@Test
	public void printsStack(){
		StackAr a = new StackAr();
		a.push(3);
		a.push(5);
		a.push(11);
		String res = a.toString();
		assertEquals("[3,5,11]", res);
	}
}
