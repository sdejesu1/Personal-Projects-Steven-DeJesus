// import PrintWriter and exceptions for output file
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
// import scanner for reading file
import java.util.Scanner;
// import File
import java.io.File;

/** Steven De Jesus
 * 
 * This program opens a file of integers (numbers.txt)
 * and produces an output file that contains a table with
 * each integer and an indication of the properties of the number,
 * with those being repeating numbers, even numbers, or prime.
 * 
 * This program utilizes techniques such as methods, reading
 * and writing files
 */

public class NumberTester
{
    public static void main(String[] args) throws IOException, FileNotFoundException
    {
        // create read file variable
        File numbersFile = new File("numbers.txt");
        Scanner inputFile = new Scanner(numbersFile); 

        // create output file variable
        PrintWriter outputFile = new PrintWriter("numberSummary.txt");

        // declare and initialize strings for formatting (titles)
        String stringNum = new String("Number");
        String stringRepeat = new String("Repeat Digits");
        String stringEven = new String("Even");
        String stringPrime = new String("Prime");

        outputFile.printf("%25s %25s %25s %25s", stringNum, stringRepeat, stringEven, stringPrime);
        outputFile.println();

        // write to output file (while loop) with table and hasNext
        while (inputFile.hasNext())
        {
            int fileNum = inputFile.nextInt();

            // call methods and pass fileNum parameter
            // set ifs, to make variables that are + or -
            
            // declare string variables for + or -
            String primeSign, evenSign, repeatSign;
        
            // isPrime verify
            if (isPrime(fileNum))
            {
                primeSign = "+";
            } else
            {
                primeSign = "-";
            }
            
            // isEven verify
            if (isEven(fileNum))
            {
                evenSign = "+";
            } else
            {
                evenSign = "-";
            }

            // for isRepeatedDigits convert to string to
            // compare digits

            String fileNumString = String.valueOf(fileNum);
            
            // isRepeatedDigits verify
            if (isRepeatedDigits(fileNumString))
            {
                repeatSign = ("+");
            } else
            {
                repeatSign = new String("-");
            }



            // print to the output file
            outputFile.printf("%25s %25s %25s %25s", fileNum, repeatSign, evenSign, primeSign);
            outputFile.println();
        }

        System.out.print(outputFile);
        

        // close output file
        outputFile.close();

        // close input file
        inputFile.close();

    }

    /** isPrime method that takes int
     * and returns true if number is prime
     * false otherwise
     * @params int fileNum, which accepts the parameter int values 
     * from the output file, which are the numbers from numbers.txt
     * @return a boolean value based on whether the conditions are met */

    public static boolean isPrime(int fileNum)
    {

        for (int i = 2; i < fileNum / 2; i++)
            if (fileNum % i == 0)
            {
                return false;
            } 
        return true;
    }

    /** isEven method that takes int
     * and returns true if number is even
     * false otherwise
     * @params int fileNum, which accepts the parameter int values 
     * from the output file, which are the numbers from numbers.txt
     * @return a boolean value based on whether the conditions are met */

    public static boolean isEven(int fileNum)
    {
        if (fileNum % 2 == 0)
        {
            return true;
        } else 
        {
            return false;
        }
    }

    /** isRepeatedDigits method that takes int
     * and returns true if number is prime
     * false otherwise
     * @params int fileNum, which accepts the parameter int values 
     * from the output file, which are the numbers from numbers.txt
     * @return a boolean value based on whether the conditions are met */

    public static boolean isRepeatedDigits(String fileNumString)
    {
        for (int i = 1; i < fileNumString.length(); i++)
        {
            if (fileNumString.charAt(i) == fileNumString.charAt(i-1))
            {
                return true;
            } 
        }
        return false;
    }


}