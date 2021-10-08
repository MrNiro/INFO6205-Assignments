package edu.neu.coe.info6205.union_find;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class UF_HWQUPC_Driver {
    public static int count(int n){
        UF_HWQUPC h = new UF_HWQUPC(n, true);
        Random r = new Random();
        int c = 0;

        while(h.components() > 1){
            c++;
            int i = r.nextInt(n);
            int j = r.nextInt(n);

            while(i == j){      // Avoid i = j
                j = r.nextInt(n);
            }

            if(!h.connected(i, j)){
                h.union(i, j);
            }
        }

        return c;
    }

    public static void main(String[] args){
        try {
            //Write the result into a file, and use python to do visualization later
            BufferedWriter outfile = new BufferedWriter(
                    new FileWriter(".\\src\\main\\java\\edu\\neu\\coe\\info6205\\union_find\\result.csv"));
            System.out.println("======== Create file writer success! ========\n");

            System.out.println("======== Test on Union-Found started! ========");
            System.out.println("\t\tcomponents \t using steps ");
            for(int n = 10; n <= 50000; n+=10){
                int temp_sum = 0;

                for(int i = 0; i <10; i++) {
                    // Run each n for 10 times
                    temp_sum += count(n);
                }
                int avg_m = temp_sum / 10;
                System.out.println("\t\t\t" + n + "\t\t\t" + avg_m);
                outfile.write(n + " " + avg_m + "\n");
            }

            outfile.close();
            System.out.println("\n======== Results have been written to a file! =======");
        }
        catch (IOException e) {
            System.out.println("======== Create file writer error! =======\n");
        }
    }
}
