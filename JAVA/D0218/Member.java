/**	**********************************************************************************************	
 * 	클래스 역할 : 회원정보 틀래스
 * 	클래스 속성 : id, pw, name, age, phone, gender, job, addrress
 * 	클래스 기능 : 정보출력
 ** **********************************************************************************************/
public class Member {
	
	// 멤서 속성
	String id;
	String pw;
	String name;
	int age;
	String phone;
	char gender;
	String job;
	String address;
	
	
	// 생성자 메서드 --------------------------------------------------------------------------------------
	// 속성 초기화
	// 생성자 메서드 오버로딩

	// Default 생성자 : 매개변수 X, 개발자가 속성 기본값 설정
	Member(){
		
		id		= "unknown";
		pw 		= "unknown";
		age		= 0;
		phone 	= "unknown";
		gender	= 'N';
		job		= "unknown";
		address	= "unknown";	
		
	}	
	
	Member(String id_, String pw_){
		
		// 속성명 = 저장할 값;
		id		= id_;
		pw 		= pw_;
	}
	
	Member(String id_, String pw_, String name_,String phone_){
	
		// 속성명 = 저장할 값;
		id		= id_;
		pw 		= pw_;
		name	= name_;
		phone 	= phone_;
	}
	
	Member(String id_, String pw_, String name_, int age_, 
			String phone_, char gender_, String job_, String address_){
	
		// 속성명 = 저장할 값;
		id		= id_;
		pw 		= pw_;
		age		= age_;
		phone 	= phone_;
		gender	= gender_;
		job		= job_;
		address	= address_;	
	}
	

	// 멤버/인스턴스 메서드
	/*	------------------------------------------------------------------------------------
	 *	메서드 이름	: showInfo
	 *	매개 변수들	: 없음
	 *	메서드 결과	: 없음 void
	 *	------------------------------------------------------------------------------------*/
	
	void showInfo() {
		System.out.println("===========================");
		System.out.println("회원이름 : " + name);
		System.out.println("전화번호 : " + phone);
		System.out.println("===========================");
		
		
		
	}
	
	
	
	
	
	
}
