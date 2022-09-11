/** header
 * Steven De Jesus
 * CS110 - Assignment 8
 * 04/08/2022
 */

import java.util.Scanner;
import java.io.*;
import java.util.ArrayList;

public class VehicleDriver {
    public static void main(String[] args) throws IOException {
        /** open vehicles.txt file 
         * @param file = file object that represents "Vehicles.txt"
        */
        File file = new File("Vehicles.txt");

        /** create scanner object
         * @param inputFile - scanner object that reads from the file
        */
        Scanner inputFile = new Scanner(file);

        /** create array list object which will store vehicles 
         * @param vehiclesList - array list of vehicle objects
        */
        ArrayList<Vehicle> vehiclesList = new ArrayList<Vehicle>();

        /**  loop creating Vehicle objects from text file
         * @param name - string variable to be called to make person object
         * @param address - string variable for person object
         * @param phone - string variable for person object
         * @param make - string variable for vehicle object
         * @param model - string variable for vehicle object
         * @param stringYear - string variable for vehicle object
         * @param stringMileage - string variable for vehicle object
         * @param stringNumPassengers - string variable for vehicle object
         * @param stringIsSUV - string variable for vehicle object
         * @param driverName - string variable for driver person object
         * @param driverAddress - string variable for driver person object
         * @param driverPhone - string variable for driver person object
        */
        while (inputFile.hasNext()) {
            /** have to hardcode param variables for class / object calls */

            boolean newCar;
            String vehicleType = inputFile.nextLine();

            if (vehicleType.equals("Taxi")) {
                String name = inputFile.nextLine();
                String address = inputFile.nextLine();
                String phone = inputFile.nextLine();
                String make = inputFile.nextLine();
                String model = inputFile.nextLine();
                String stringYear = inputFile.nextLine();
                String stringMileage = inputFile.nextLine();
                String stringNumPassengers = inputFile.nextLine();
                String stringIsSUV = inputFile.nextLine();
                String driverName = inputFile.nextLine();
                String driverAddress = inputFile.nextLine();
                String driverPhone = inputFile.nextLine();
                String ID = inputFile.nextLine();

                /**  convert from strings to ints and bools 
                 * @param year - int var for year
                 * @param mileage - int var for mileage
                 * @param numPassengers - int var for num passengers
                 * @param isSUV - bool var for if suv or not
                 * @param owner - person object representing owner of car
                 * @param driver - person object representing driver of car
                */
                int year = Integer.parseInt(stringYear);
                int mileage = Integer.parseInt(stringMileage);
                int numPassengers = Integer.parseInt(stringNumPassengers);
                boolean isSUV = Boolean.parseBoolean(stringIsSUV);
                Person owner = new Person(name, address, phone);
                Person driver = new Person(driverName, driverAddress, driverPhone);
                vehiclesList.add(new Taxi(owner, make, model, year, mileage, numPassengers, isSUV, ID, driver));
                newCar = true;
            } else if (vehicleType.equals("Truck")) {
                String name = inputFile.nextLine();
                String address = inputFile.nextLine();
                String phone = inputFile.nextLine();
                String make = inputFile.nextLine();
                String model = inputFile.nextLine();
                String stringYear = inputFile.nextLine();
                String stringMileage = inputFile.nextLine();
                String stringCapacity = inputFile.nextLine();
                String stringNumAxles = inputFile.nextLine();
                int year = Integer.parseInt(stringYear);
                int mileage = Integer.parseInt(stringMileage);
                int capacity = Integer.parseInt(stringCapacity);
                int numAxles = Integer.parseInt(stringNumAxles);
                Person owner = new Person(name, address, phone);
                vehiclesList.add(new Truck(owner, make, model, year, mileage, capacity, numAxles));
                newCar = true;
            } else if (vehicleType.equals("Automobile")) {
                String name = inputFile.nextLine();
                String address = inputFile.nextLine();
                String phone = inputFile.nextLine();
                String make = inputFile.nextLine();
                String model = inputFile.nextLine();
                String stringYear = inputFile.nextLine();
                String stringMileage = inputFile.nextLine();
                String stringNumPassengers = inputFile.nextLine();
                String stringIsSUV = inputFile.nextLine();
                int year = Integer.parseInt(stringYear);
                int mileage = Integer.parseInt(stringMileage);
                int numPassengers = Integer.parseInt(stringNumPassengers);
                boolean isSUV = Boolean.parseBoolean(stringIsSUV);
                Person owner = new Person(name, address, phone);
                vehiclesList.add(new Automobile(owner, make, model, year, mileage, numPassengers, isSUV));
                newCar = true;
            }
        }

        /** close text file */
        inputFile.close();

        /** find two oldest cars in ArrayList of vehicles and store them in new ArrayList 
         * @param oldestVehicles - arraylist of vehicles for oldest ones
        */
        ArrayList<Vehicle> oldestVehicles = new ArrayList<Vehicle>();
        for (Vehicle v : vehiclesList) {
            if (oldestVehicles.size() == 0) {
                oldestVehicles.add(v);
            } else if (oldestVehicles.size() > 0 && v.getYear() < oldestVehicles.get(0).getYear()) {
                oldestVehicles.set(0, v);
            } else if (oldestVehicles.size() > 0 && v.getYear() == oldestVehicles.get(0).getYear()) {
                oldestVehicles.add(v);
            }
        }

        // display the old vehicles to be sold
        System.out.println("Vehicles to be sold: \n");
        int count = 1;
        for (Vehicle v : oldestVehicles) {
            if (v instanceof Taxi) {
                System.out.println("TAXI: " + count + ": " + v.toString() + "\n");
            } else if (v instanceof Truck) {
                System.out.println("TRUCK: " + count + ": " + v.toString() + "\n");
            } else if (v instanceof Automobile) {
                System.out.println("AUTOMOBILE: " + count + ": " + v.toString() + "\n");
            }
            count++;
        }

    }
}