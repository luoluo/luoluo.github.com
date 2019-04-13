---
layout: post
title: "Hash in Java"
date: 2013-08-14 20:50
comments: true
categories: [Languages]
---
Hash is a useful tool in everyday programming work. Here is a brief summary.
###HashMap & HashSet
####HashSet
	import java.util.HashSet;
	import java.util.Iterator;

	public class hashSetTest {
	    private static final HashSet<String> set = new HashSet<String>() {
	        {
	            add("A");
	            add("B");
	            add("C");
	            add("D");
	            add("E");
	        }
	    };
	    public static void main(String[] argc) {
	        if(set.isEmpty()) {
	            System.out.println("is set empty? " + set.isEmpty());
	        }
	        if(set.contains("A")) {
	            System.out.println("is set contains A? " + set.contains("A"));
	        }
	
	        Iterator i = set.iterator();
	        while(i.hasNext()) {
	            System.out.println("has values: " + i.next());
	        }
	
	        set.remove("A");
	        if(set.contains("A")) {
	            System.out.println("is set contains A? " + set.contains("A"));
	        }
	
	        System.out.println("set size = " + set.size());
	        set.clear();
	        System.out.println("set size = " + set.size());
	    }
	
	}
####Run result
	is set contains A? true
	has values: D
	has values: E
	has values: A
	has values: B
	has values: C
	set size = 4
	set size = 0

	Process finished with exit code 0
####HashMap
	import java.util.HashMap;
	
	public class hashTest {
	    private static final HashMap<String, Integer> map = new HashMap<String, Integer> () {
	        {
	            put("A", 1);
	            put("B", 2);
	            put("C", 3);
	            put("D", 4);
	        }
	
	    };
	    public static void main(String[] argc) {
	        if(map.containsKey("A")) {
	            System.out.println("is map Contains key A? " + map.containsKey("A"));
	        }
	        if(map.containsValue(1)) {
	            System.out.println("is map Contains value 1? " + map.containsKey("A"));
	        }
	        if(map.isEmpty()){
	            System.out.println("is map empty? " + map.isEmpty());
	        }
	        System.out.println("map size = " + map.size());
	        for(String key : map.keySet()) {
	            System.out.println(key + "->" + map.get(key));
	        }
	        
	        map.clear();
	        if(map.isEmpty()){
	            System.out.println("is map empty? " + map.isEmpty());
	        }
	    }
	}
####Run result
	is map Contains key A? true
	is map Contains value 1? true
	map size = 4
	D->4
	A->1
	B->2
	C->3
	is map empty? true

	Process finished with exit code 0
####Well, that's all.
