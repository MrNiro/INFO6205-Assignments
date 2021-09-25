package edu.neu.coe.info6205.sort;

import edu.neu.coe.info6205.sort.elementary.InsertionSort;
import edu.neu.coe.info6205.util.*;

import java.util.Random;

public class InsertionGrowthTest {
    public static final Config config =
            ConfigTest.setupConfig("true", "0", "1", "", "");
    public static Timer timer = new Timer();

    public static void TimeTestForFourInsertionSort(int n){
        Helper<Integer> helper = HelperFactory.create("InsertionSort", n, config);
        SortWithHelper<Integer> sorter = new InsertionSort<>(helper);
        helper.init(n);

        //====================== random array ===========================//
        Integer[] xs = helper.random(Integer.class, r -> r.nextInt(1000));
        double time_1 = timer.repeat(10,
                () -> xs,
                sorter::sort,
                sorter::preProcess,
                sorter::postProcess);


        //====================== ordered array ===========================//
        Integer[] ys = new Integer[n];
        for(int i = 0; i < n; i++){ ys[i] = i; }
        double time_2 = timer.repeat(10,
                () -> ys,
                sorter::sort,
                sorter::preProcess,
                sorter::postProcess);


        //====================== partially-ordered array ===========================//
        Integer[] ws = new Integer[n];
        int each_part_num = n / 10;
        int part_count = 1;
        Random r = new Random();
        for(int i = 0; i < n; i++){
            if(i > part_count * each_part_num)
                part_count += 1;
            ws[i] = each_part_num * part_count + r.nextInt(each_part_num);
        }
        double time_3 = timer.repeat(10,
                () -> ws,
                sorter::sort,
                sorter::preProcess,
                sorter::postProcess);


        //====================== inverse array ===========================//
        Integer[] zs = new Integer[n];
        for(int i = 0; i < n; i++){ zs[i] = n - i; }
        double time_4 = timer.repeat(10,
                () -> zs,
                sorter::sort,
                sorter::preProcess,
                sorter::postProcess);


        System.out.println("\n==============Sort time(ms) when n = " + n + " ==============");
        System.out.printf("\trandom array: \t\t\t%.4f ms\n", time_1);
        System.out.printf("\tordered array: \t\t\t%.4f ms\n", time_2);
        System.out.printf("\tpartially-ordered: \t\t%.4f ms\n", time_3);
        System.out.printf("\tinverse array: \t\t\t%.4f ms\n", time_4);
    }

    public static void main(String[] args) {
        for(int n = 1000; n <= 32000; n *= 2) {
            TimeTestForFourInsertionSort(n);
        }
    }
}
