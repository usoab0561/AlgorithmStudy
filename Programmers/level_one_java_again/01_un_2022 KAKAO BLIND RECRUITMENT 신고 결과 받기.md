https://programmers.co.kr/learn/courses/30/lessons/92334#

```java
import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, HashSet<String>> map = new HashMap<>();
        Map<String, Integer> idxMap = new HashMap<>();
 
        for (int i = 0; i < id_list.length; i++) {
            String name = id_list[i];
            map.put(name, new HashSet<>());
            idxMap.put(name, i);
        }
 // continue
        for (String s : report) {
            String[] str = s.split(" ");
            String from = str[0];
            String to = str[1];
            map.get(to).add(from);
        }
 
        for (int i = 0; i < id_list.length; i++) {
            HashSet<String> send = map.get(id_list[i]);
            if (send.size() >= k) {
                for (String name : send) {
                    answer[idxMap.get(name)]++;
                }
            }
        }
        return answer;
    }
}
```


```java
import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        int[] reported_rate = new int[id_list.length];
        Map<String, Integer> idxMap = new LinkedHashMap<String, Integer>();
        List<HashSet<String>> list = new ArrayList<HashSet<String>>();

        
        for (int i = 0; i < id_list.length; i++){
            String name = id_list[i];
            idxMap.put(name, i);
            list.add(new HashSet<String>());
        }
        System.out.println(list.get(0));
        for (int i = 0; i < report.length; i++){
            String[] str = report[i].split(" ");
            String from = str[0];
            String to = str[1];
            //System.out.println(list.get(i));
            //list[i].add(to);
        }
        System.out.println(list);
//         Map<String, HashSet<String>> map = new HashMap<>();
//         Map<String, Integer> idxMap = new HashMap<>();
 
//         for (int i = 0; i < id_list.length; i++) {
//             String name = id_list[i];
//             map.put(name, new HashSet<>());
//             idxMap.put(name, i);
//         }
//  // continue
//         for (String s : report) {
//             String[] str = s.split(" ");
//             String from = str[0];
//             String to = str[1];
//             map.get(to).add(from);
//         }
        
//         System.out.println(map);
//         for (int i = 0; i < id_list.length; i++) {
//             HashSet<String> send = map.get(id_list[i]);
//             if (send.size() >= k) {
//                 for (String name : send) {
//                     answer[idxMap.get(name)]++;
//                 }
//             }
//         }
        return answer;
    }
}

```
