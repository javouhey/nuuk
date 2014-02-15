package javouhey;

import java.net.URL;
import org.junit.Test;
import static org.junit.Assert.*;

public class ByteCounterTest {

    @Test
    public void testImageFile() {
        URL url = this.getClass().getClassLoader().getResource("javouhey/1.png");
        assertNotNull(url);
        //System.out.println(url + " -> " + url.getPath());
        assertEquals(17905, ByteCounter.fileSizeOf(url.getPath()));
    }

    @Test
    public void testZipFile() {
        URL url = this.getClass().getClassLoader().getResource("javouhey/goo2.zip");
        assertNotNull(url);
        //System.out.println(url + " -> " + url.getPath());
        assertEquals(3143, ByteCounter.fileSizeOf(url.getPath()));
    }
}
