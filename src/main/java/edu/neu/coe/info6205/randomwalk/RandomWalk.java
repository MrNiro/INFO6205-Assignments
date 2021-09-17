/*
 * Copyright (c) 2017. Phasmid Software
 */

package edu.neu.coe.info6205.randomwalk;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class RandomWalk {

    private int x = 0;
    private int y = 0;

    private final Random random = new Random();

    /**
     * Private method to move the current position, that's to say the drunkard moves
     *
     * @param dx the distance he moves in the x direction
     * @param dy the distance he moves in the y direction
     */
    private void move(int dx, int dy) {
        // TO BE IMPLEMENTED
        x += dx;
        y += dy;
    }

    /**
     * Perform a random walk of m steps
     *
     * @param m the number of steps the drunkard takes
     */
    private void randomWalk(int m) {
        // TO BE IMPLEMENTED
        for(int step = 0; step < m; step++){
            randomMove();
        }
    }

    /**
     * Private method to generate a random move according to the rules of the situation.
     * That's to say, moves can be (+-1, 0) or (0, +-1).
     */
    private void randomMove() {
        boolean ns = random.nextBoolean();
        int step = random.nextBoolean() ? 1 : -1;
        move(ns ? step : 0, ns ? 0 : step);
    }

    /**
     * Method to compute the distance from the origin (the lamp-post where the drunkard starts) to his current position.
     *
     * @return the (Euclidean) distance from the origin to the current position.
     */
    public double distance() {
        // TO BE IMPLEMENTED
        return Math.sqrt(x * x + y * y);
    }

    /**
     * Perform multiple random walk experiments, returning the mean distance.
     *
     * @param m the number of steps for each experiment
     * @param n the number of experiments to run
     * @return the mean distance
     */
    public static double randomWalkMulti(int m, int n) {
        double totalDistance = 0;
        for (int i = 0; i < n; i++) {
            RandomWalk walk = new RandomWalk();
            walk.randomWalk(m);
            totalDistance = totalDistance + walk.distance();
        }
        return totalDistance / n;
    }

    public static void main(String[] args) {
        try {
            //Write the result into a file, and use python to do visualization later
            BufferedWriter outfile = new BufferedWriter(
                    new FileWriter(".\\src\\main\\java\\edu\\neu\\coe\\info6205\\randomwalk\\result.csv"));
            System.out.println("==================Create file writer success!================\n");

            int m = 1000;
            // run m times for each n and take the average distance
            for(int n = 1; n < 5000; n += 10) {
                double meanDistance = randomWalkMulti(n, m);
                System.out.println(n + " steps: distance = " + meanDistance + " over " + m + " experiments");

                outfile.write(n + " " + meanDistance + "\n");
            }
            outfile.close();

            System.out.println("\n==================Results have been written to a file!================");
        }
        catch (IOException e) {
            System.out.println("==================Create file writer error!==================\n");
        }
    }

}
