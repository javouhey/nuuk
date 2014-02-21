package javouhey;

import java.util.*;

class Pair<S, T> {
    public S left;
    public T right;
    private Pair(S s, T t) {
        this.left = s; 
        this.right = t;
    }
    public static <S, T> Pair of(S s, T t) {
        return new Pair<S, T>(s, t);
    }
    public String toString() {                                                         
        return "" + this.left + "," + this.right;                              
    }
}

public class NumberPairs {
    /**
     * Parses <code>1,2,3,4;50</code>
     */
    static class LineParser {
	    public final List<Integer> numlists;
	    public final int target;
	    
	    public LineParser(String line) {
	        String[] segments = line.split(";");
	        String[] rawnumlist = segments[0].split(",");
	        this.target = Integer.parseInt(segments[1]);
	        List<String> list1 = Arrays.asList(rawnumlist);
	        this.numlists = new ArrayList<Integer>(list1.size()); 
	        for (String item: list1) {
	            numlists.add(Integer.parseInt(item));
	        }
		}	
	}

    public static List<Pair<Integer,Integer>> combinations(int max) {
        List<Pair<Integer,Integer>> p = new ArrayList<Pair<Integer, Integer>>();
        for (int i=0; i<max-1; i++) {                                               
            for (int j=i+1; j<max; j++) {                                           
                p.add(Pair.of(i, j));                                                     
            }                                                                           
        }
        return p;
    }

    public static String solution(String line) {
        LineParser parser = new LineParser(line);
        List<Pair<Integer,Integer>> combos = combinations(parser.numlists.size());                                            

        List<Pair<Integer, Integer>> result = new ArrayList<Pair<Integer, Integer>>();
        for(Pair<Integer, Integer> pair: combos) {
            if(parser.target == parser.numlists.get(pair.left) + parser.numlists.get(pair.right)) {
                result.add(Pair.of(parser.numlists.get(pair.left), 
                                   parser.numlists.get(pair.right)));
			}
		}

        if (result.size() == 0)
            return "NULL";
        else {
	        StringBuilder builder = new StringBuilder();
            int i=0; int m=result.size()-1; 
	        for(Pair<Integer, Integer> pair: result) {
                builder.append(pair.toString());
                if(i!=m) 
                    builder.append(";");
                i++;
			}
            return builder.toString();
        }
    }
}
