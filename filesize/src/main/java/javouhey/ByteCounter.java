package javouhey;

import java.nio.file.Path;                                                           
import java.io.InputStream;                                                          
import java.io.IOException;
import static java.nio.file.Paths.get;
import static java.nio.file.Files.newInputStream;                                    
public class ByteCounter {
    public static int fileSizeOf(String fileName) {
        Path p2 = get(fileName);
        //System.out.println(p2.getFileName());
        int retval = 0;
        int MAX = 2048;
        byte[] buffer = new byte[MAX];
        try (InputStream is = newInputStream(p2)) {
            int read = 0;
            while((read = is.read(buffer, 0, MAX)) != -1) {
                //System.out.println("--->" + read);
                retval += read;
            } 
        } catch(IOException ioe) {
            throw new RuntimeException(ioe);
        }
        return retval;
    }

    public static void main(String[] args) {
        System.out.println(args);

        if (args.length == 0)
            System.out.println(0);

        System.out.println(fileSizeOf(args[0]));
    }
}
