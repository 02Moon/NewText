### 数组

> 最常见的数组使用
>
> ```java
> int[] Array;
> ```
>
> 数组的初始化方法有很多，最常见的
>
> ```java
> int[] Array = new int[10];
> ```
>
> ```java
> int Array[] = new int[] {1, 2, 3, 4, 5};
> ```
>
> 数组的遍历
>
> 1. 使用 for 循环
>
> ```java
> for(int i = 0;i<Array.length;i++){
> 	System.out.println(Array[i]);
> }
> ```
>
> 2. 使用 for-each 循环
>
> ```java
> for(int element : Array){
> 	System.out.println(element);
> }
> ```
>
> 数组转换成List
>
> - 最原始的方法，通过循环遍历将数组添加到 List 中
> - 通过 Arrays 类的 `asList()` 方法
> ```java
> List<Integer> aList = Arrays.asList(anArray);
> ```
> - Arrays.asList 的参数需要的是 Integer 数组，而 anArray 目前是 int 类型，需要另一种方式
>
> ```java
> List<Integer> aList = Arrays.stream(anArray).boxed().collect(Collectors.toList());
> ```
>
> 排序
>
> ```java
> String[] yetAnotherArray = new String[] {"A", "E", "Z", "B", "C"};
> Arrays.sort(yetAnotherArray, 1, 3,
>                 Comparator.comparing(String::toString).reversed());
> ```
>
> 二分查找
>
> ```java
> int[] anArray = new int[] {1, 2, 3, 4, 5};
> int index = Arrays.binarySearch(anArray, 4);
> ```
>
