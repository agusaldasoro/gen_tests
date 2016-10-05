package org.autotest;

import static org.junit.Assert.*;

import org.junit.Test;

public class TestStackAr {

	@Test
	public void test0() {
		StackAr s = new StackAr();
		s.push(new Integer(1));
		s.top();
		s.pop();
		s.size();
		s.isEmpty();
		s.isFull();
		s.toString();
	}

	@Test
	public void test1() {
		StackAr s = new StackAr(30);
		Object o = new Object();
		s.push(o);
		s.top();
		s.pop();
		s.toString();
	}

	@Test
	public void test2() {
		StackAr s = new StackAr(100);
		s.push(new Integer(1));
		s.push(new Integer(2));
		s.push(new Integer(65465));
		s.push(new Integer(35));
		s.isEmpty();
		s.pop();
		s.isEmpty();
		s.pop();
		s.isEmpty();
		s.pop();
		s.pop();
		s.isEmpty();
		s.toString();
	}

	@Test
	public void test3() {
		StackAr s = new StackAr(1);
		s.push(new String("gfdgfg"));
		s.isEmpty();
		s.toString();
		s.top();
	}

	@Test
	public void test4() {
		StackAr s = new StackAr(0);
		s.size();
		s.isEmpty();
		s.toString();
	}

	@Test
	public void testAA() {
		StackAr s = new StackAr();
		s.size();
		s.isEmpty();
		s.toString();
	}

	@Test
	public void testNulls() {
		StackAr s = new StackAr();
		s.push(null);
		s.top();
		s.size();
		s.isEmpty();
		s.toString();
	}

	@Test
	public void fullStack2() {
		StackAr s = new StackAr(11);
		s.push(new Integer(1));
		s.push(new Integer(1));
		s.push(new Integer(2));
		s.push(new Integer(65465));
		s.push(new Integer(65465));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.isEmpty();
		s.top();
		s.toString();
	}

	@Test
	public void fullStack() {
		StackAr s = new StackAr(12);
		s.push(new Integer(1));
		s.push(new Integer(1));
		s.push(new Integer(2));
		s.push(new Integer(65465));
		s.push(new Integer(65465));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.push(new Integer(35));
		s.isEmpty();
		s.top();
		s.toString();
	}

	@Test
	public void test() {
		StackAr a = new StackAr();
		a.toString();
	}

	@Test (expected = IllegalArgumentException.class)
	public void failureTest() {
		StackAr a = new StackAr(-1);
		a.toString();
	}

	
	@Test
	public void sizeTest() {
		StackAr a = new StackAr();
		a.size();
		a.toString();
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
	public void stackOfArray() {
		StackAr a = new StackAr();
		Object[] o = new Object[2];
		a.push(o);
		a.top();
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
	public void isEqualTest(){
		StackAr a = new StackAr();
	}

	@Test
	public void isNullEqualTest(){
		StackAr a = new StackAr();
		StackAr b = null;
	}

	@Test
	public void differentClassEqualTest(){
		StackAr a = new StackAr();
		int b = 3;
	}

	@Test
	public void sameClassEqualTest(){
		StackAr a = new StackAr();
		StackAr b = new StackAr();
		b.push(2);
	}

	@Test
	public void sameClassAndElemsEqualTest(){
		StackAr a = new StackAr();
		StackAr b = new StackAr();
		a.push(2);
		b.push(2);
	}


	@Test
	public void sameClassAndElemsDiEqualTest(){
		StackAr a = new StackAr();
		StackAr b = new StackAr();
		a.push(2);
		b.push(2);
		b.pop();
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

