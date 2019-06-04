// Aleks Calderon
//6.4.2019
//Problem 1,2 M9




class Animal {
  public void animalSound() {
    System.out.println("The animal makes a sound");
  }
}

class Pig extends Animal {
  public void animalSound() {
    System.out.println("The pig says: wee wee");
  }
}

class Dog extends Animal
{
  public void animalSound()
  {
    System.out.println("The dog says: woof");
  }
  
}

class Cat extends Animal
{
  public void animalSound()
  {
    System.out.println("The cat says: meow");
  }
}

puublic class mainClass
{
  public static void main(String [] args)
  {
    Animal pigObj = new Pig();
    Animal catObj = new Cat();
    Animal dogObj = new Dog();
    
    pigObj.animalSound();
    catObj.animalSound();
    dogObj.animalSound();
    
  }
}