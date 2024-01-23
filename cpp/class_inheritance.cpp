#include<iostream>
using namespace std;
class Vehicle
{
	private :
	char color[15];
	

public:
	int wheels;
	Vehicle(){

	}
	void start(){
		cout << "Vehicle started\n";
	}
	void stop()
	{
		cout << "Vehicle stop\n";
	}
	void info(){
		cout << "vehicle info\n";
	}
};



class Bike : public Vehicle // inheritance
{
	
public:
	Bike(){
		wheels=2;
		cout << "inside bike constructor\n";

	}

	void start(){
		cout << "Bike started\n";
	}
	void stop()
	{
		cout << "Bike stop\n";
	}

	void info(){
		cout<<"Bike info wheels "<<wheels << "\n";
	}
};
class Car : public Vehicle  // inheritance
{
public:
	Car(){
		int	wheels=4;
	}
	void start(){
		cout << "Car started\n";
	}
	void stop()
	{
		cout << "Car stop\n";
	}
 
};
int main()
{

	Vehicle v = Vehicle(); // creating object of a class
    v.start();
	v.info();
	v.stop();


	Bike b = Bike();
	b.start();
	b.info();
	b.stop();


	Car c = Car();
	c.start();
	c.info();
	c.stop();

   
    Vehicle v1 = Bike();
    // Bike b1 = Vehicle(); not allowed creating a child object from parent



	return 0;
}