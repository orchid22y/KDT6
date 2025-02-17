/*	************************************************************************************
 *  배열(Array) 선언 및 활용
 *  	: 동일한 데이터 타입의 데이터를 연속된 메모리 공간에 저장하는 것
 *  	: 배열 객체 속성과 메서드
 *	************************************************************************************/

public class EX_Array05 {

	public static void main(String[] args) {
		// 배열 객체 생성
		int values[] = new int[5];
		int age =100;			// age는 객체가 아님, 메서드,속성 없음
		String name = "hong";	// 객체
		
		
		
		// 배열 객체명.속성명
		System.out.println("배열의 원소 갯수: "+values.length);		// 변수의 원소 갯수: 5
		System.out.println("문자열의 원소 갯수: "+ name.length());	// 문자열의 원소 갯수: 4
		// 배열 객체명.메서드명()	//함수이기 때문에 '()'필수
		System.out.println(values.toString());					// [I@13221655
	}

}
