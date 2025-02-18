package com.data;



/**	*************************************************************************************
 * 	클래스 역할	: 판매 제품 정보 저장
 * 	클래스 이름	: Product
 * 	클래스 속성	: 제품코드, 제품명, 단가, 수량
 * 	클래스 기능	: 제품 정보 출력 기능
 * 			  제품코드에 따른 가격 안내 기능
 * 			  제품코드에 따른 수량 안내 기능 
 *	*************************************************************************************/


public class Product {
	// -----------------------------------------------------------------------------------
	// 멤버 속성(변수)
	// -----------------------------------------------------------------------------------
	private String 	code;	// 제품코드
	private String 	pname;	// 제품명
	private int		price;	// 단가
	private int		count;	// 수량
	
	
	// -----------------------------------------------------------------------------------
	// 생성자 메서드 오버로딩
	// -----------------------------------------------------------------------------------
	
	public Product() {
		this("Unknown","Unknown",0,0);
	}
	
	
	/**
	 * @param code
	 * @param pname
	 * @param price
	 * @param count
	 */
	public Product(String code, String pname, int price, int count) {
		this.code = code;
		this.pname = pname;
		this.price = price;
		this.count = count;
	}
	
	/**
	 * @param code
	 * @param pname
	 * @param count
	 */
	public Product(String code, String pname, int price) {
		this.code = code;
		this.pname = pname;
		this.price = price;

	}
	
	/**
	 * @param code
	 * @param pname

	 */
	public Product(String code, String pname) {
		this.code = code;
		this.pname = pname;
	}

	
	
	// -----------------------------------------------------------------------------------
	// getter/setter 메서드
	// -----------------------------------------------------------------------------------
	public String getCode() {
		return code;
	}


	public String getPname() {
		return pname;
	}


	public int getPrice() {
		return price;
	}


	public int getCount() {
		return count;
	}


	public void setPrice(int price) {
		this.price = price;
	}


	public void setCount(int count) {
		this.count = count;
	}
	
	
	// -----------------------------------------------------------------------------------
	// 인스턴스 메서드 : 객체 생성 후 사용 가능한 메서드
	// -----------------------------------------------------------------------------------
	
	
	// 제품코드에 따른 수량 안내 기능
	
	/** -----------------------------------------------------------------------------------
	 * 	메서드기능: 제품정보 출력 기능
	 * 	메서드이름:	 showInfo()
	 * 	매개변수들: 없음
	 * 	메서드결과: void
	 * 	접근지정자: public ==> 패키지가 달라도 사용 가능
	 *	-----------------------------------------------------------------------------------*/

	public void showInfo() {
		
		System.out.println("----------------------");
		System.out.println("[" + this.code + "]");
		System.out.println("----------------------");
		System.out.println("제품명" + this.pname);
		System.out.println("수 량" + this.count);
		System.out.println("단 가" + this.price);
		System.out.println("----------------------");
				
	}
	
	
	/** -----------------------------------------------------------------------------------
	 * 	메서드기능: 제품코드에 따른 가격 안내 기능
	 * 	메서드이름:	 searchPrice()
	 * 	매개변수들: String code
	 * 	메서드결과: int
	 * 	접근지정자: public
	 *	-----------------------------------------------------------------------------------*/


	public int searchPrice(String code) {
		return this.price;
	}
	
	/** -----------------------------------------------------------------------------------
	 * 	메서드기능: 제품코드에 따른 수량 안내 기능
	 * 	메서드이름:	 searchCount()
	 * 	매개변수들: String count
	 * 	메서드결과: int
	 * 	접근지정자: default ==> 같은 패키지 안에서만 사용가능 
	 *	-----------------------------------------------------------------------------------*/


	int searchCount(String code) {
		return this.count;
	}

}






