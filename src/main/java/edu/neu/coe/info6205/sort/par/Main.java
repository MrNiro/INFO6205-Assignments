package edu.neu.coe.info6205.sort.par;

import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.concurrent.ForkJoinPool;

/**
 * This code has been fleshed out by Ziyao Qiao. Thanks very much.
 * TODO tidy it up a bit.
 */
public class Main {

    public static void SortingTest(int array_length, int threads_num, ForkJoinPool MyPool){
        int[] array = new int[(int) array_length];
        Random random = new Random();
        try {
            FileOutputStream fis =
                    new FileOutputStream("./src/result_" + threads_num + "_" + array_length / 10000 + "w.csv");
            OutputStreamWriter isr = new OutputStreamWriter(fis);
            BufferedWriter bw = new BufferedWriter(isr);
            bw.write("cutoff size(percent of array)  sorting time(ms)\n");

            // Warm up
            for (int t = 0; t < 10; t++) {
                for (int i = 0; i < array.length; i++)
                    array[i] = random.nextInt(10000000);
                ParSort.sort(array, 0, array.length, MyPool);
            }

            for (int j = 1024; j >= 1; j /= 2) {
                ParSort.cutoff = (array_length / j);

                long time;
                long startTime = System.currentTimeMillis();
                // Sort 10 times with different arrays
                for (int t = 0; t < 10; t++) {
                    for (int i = 0; i < array.length; i++) array[i] = random.nextInt(10000000);
                    ParSort.sort(array, 0, array.length, MyPool);
                }
                long endTime = System.currentTimeMillis();
                time = (endTime - startTime);

                double cutoff_percent = (double) ParSort.cutoff / array_length;
                double avg_time = (double) time / 10;
                System.out.printf("threads num: %d    cutoff percent: 1/%d    cutoff size: %d    average time: %.3f\n",
                        threads_num, j, ParSort.cutoff, avg_time);
//                System.out.println("cutoff：" + (ParSort.cutoff) + "\t\t10 times Time:" + time + "ms");

                String content = cutoff_percent + " " + avg_time + "\n";
                bw.write(content);
                bw.flush();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        processArgs(args);

        // Set up array size
        int array_length = 4000000;

        while(array_length <= 4000000) {
            int threads_num = 8;
            while (threads_num <= 1024) {
                ForkJoinPool MyPool = new ForkJoinPool(threads_num);
                //System.setProperty("java.util.concurrent.ForkJoinPool.common.parallelism", "" + threads_num);
                System.out.println("\nArray length: " + array_length / 10000 + "w");
                System.out.println("Degree of parallelism: " + MyPool.getParallelism());

                SortingTest(array_length, threads_num, MyPool);

                threads_num *= 2;
            }
            array_length += 2000000;
        }
    }

    private static void processArgs(String[] args) {
        String[] xs = args;
        while (xs.length > 0)
            if (xs[0].startsWith("-")) xs = processArg(xs);
    }

    private static String[] processArg(String[] xs) {
        String[] result = new String[0];
        System.arraycopy(xs, 2, result, 0, xs.length - 2);
        processCommand(xs[0], xs[1]);
        return result;
    }

    private static void processCommand(String x, String y) {
        if (x.equalsIgnoreCase("N")) setConfig(x, Integer.parseInt(y));
        else
            // TODO sort this out
            if (x.equalsIgnoreCase("P")) //noinspection ResultOfMethodCallIgnored
                ForkJoinPool.getCommonPoolParallelism();
    }

    private static void setConfig(String x, int i) {
        configuration.put(x, i);
    }

    @SuppressWarnings("MismatchedQueryAndUpdateOfCollection")
    private static final Map<String, Integer> configuration = new HashMap<>();


}
