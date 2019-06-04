//Aleks Calderon
//6.4.2019
//Problem 3 M9



class Bank{  
	float getRateOfInterest(){return 0;}  

}  

class SBI extends Bank{  
	float getRateOfInterest(){return 8.4f;}  

}  

class ICICI extends Bank{  
	float getRateOfInterest(){return 7.3f;}  

}  

class AXIS extends Bank{  
	float getRateOfInterest(){return 9.7f;}  

} 

class ABDC extends Bank{
  float getRateOfInterest(){return 6.3f;}
  
  
}

  public class TestPolymorphism{  
	public static void main(String args[]){  
		Bank b;  
		b=new SBI();  
		System.out.println("SBI Rate of Interest: "+b.getRateOfInterest());  
		b=new ICICI();  
		System.out.println("ICICI Rate of Interest: "+b.getRateOfInterest());  
		b=new AXIS();  
		System.out.println("AXIS Rate of Interest: "+b.getRateOfInterest()); 
      	b=new ABDC();
      	System.out.println("ABDC Rate of Interest: "+b.getRateOfInterest());
	}  
}  
