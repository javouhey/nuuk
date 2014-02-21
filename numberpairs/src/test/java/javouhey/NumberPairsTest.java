package javouhey;

import java.net.URL;
import org.junit.Test;
import static org.junit.Assert.*;

public class NumberPairsTest {

    @Test
    public void test1() {
        String res = NumberPairs.solution("1,2,3,4,6;5");
        System.out.println(res);
        assertEquals("1,4;2,3", res);
    }

    @Test
    public void test2() {
        String res = NumberPairs.solution("1,2,3,4;50");
        System.out.println(res);
        assertEquals("NULL", res);
    }

    @Test
    public void test3() {
        String res = NumberPairs.solution("2,4,5,6,9,11,15;20");
        System.out.println(res);
        assertEquals("5,15;9,11", res);
    }
}
