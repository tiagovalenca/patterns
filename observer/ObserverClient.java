package com.observer;


public class ObserverClient {
	public static void main(String args[]){
		Blogger observable = new Blogger();
		BlogReader observer = new BlogReader();
		 
		observable.addObserver(observer);
		observable.setPost("O padr�o de design observer � show bb!");
		if((observer.getPost() == "O padr�o de design observer � show bb!")) {
			System.out.println("O Leitor visualizou a not�cia: " + observer.getPost());
		}
	}
}
