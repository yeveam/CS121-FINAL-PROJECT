# CICS Room Reservation (CS121-FINAL-PROJECT)
	➡️SHAIAME D. GRANADOS
	➡️IT-2106
	➡️CS121: ADVANCE COMPUTER PROGRAMMING

## **I. PROJECT OVERVIEW**
    The CICS Room Reservation System has been developed to address the challenges of room scheduling and management within the College of Informatics and Computing Sciences (CICS). The primary goal of the system is to provide a digital platform where students, professors, and staff can easily view the availability of classrooms and other spaces, make reservations, and manage their booking status. It aims to streamline the entire process of room reservation, minimizing human error, double bookings, and inefficient use of room space. The system supports the organization's objectives of improving facility management, optimizing space usage, and enhancing operational efficiency within CICS.
    
    The system's boundaries define the features it includes and excludes, helping to set clear expectations. The included features allow users to view available rooms within the CICS building, reserve a room for a specific period, cancel a previously made reservation, and view rooms that are currently reserved. Additionally, access to the system is restricted to authenticated users, either an admin or a guest, through a login system. However, there are excluded features that are outside the scope of this system. It does not include a Graphical User Interface (GUI), such as JFrames or web interfaces, as it is a console application. The system also does not support advanced user roles, as it only differentiates between admin and guest users, without any additional levels of privilege or functionality. Furthermore, it does not provide external integration with systems like email notifications or calendar applications. The target users of this system are CICS students, professors, and staff. CICS students can use the system to reserve rooms for group studies or events, while professors may need rooms for lectures, seminars, or meetings. CICS staff can also use the system for various internal administrative purposes or meetings.
    
    The system aims to achieve the following measurable outcomes within a specified timeframe:
      - Improve room reservation efficiency and manage room availability for students, professors, and staff within CICS.
      - Reduce room reservation processing time to under 2 minutes by the end of the third month.
      - The project will be implemented using simple, yet effective software development practices tailored to the needs of the CICS community.
      - The project supports the college's mission of improving operational processes and optimizing the use of educational facilities.
      - The system is expected to be fully functional within three months, with performance benchmarks assessed at 1, 3, and 6 months post-implementation.

	
## **II.PYTHON CONCEPTS AND LIBRARIES**
    The CICS Room Reservation System is built using fundamental Python concepts and libraries that ensure simplicity, efficiency, and scalability:
    
    Classes and Objects
    The system uses classes to represent various entities like rooms, users, and reservations. For example, the Room class holds the details of a room, and the Reservation class manages room bookings. Objects are instances of these classes, such as a Room object representing a specific room or a Reservation object managing the booking status.
    
    Conditionals
    The system uses if-else statements to handle different scenarios such as checking whether a room is available or not, processing a user’s login credentials, or confirming room reservations.
    
    Loops
    The program uses for loops to iterate through the list of rooms and display available or reserved rooms. This enables efficient querying of room availability.
    
    Dictionaries
    A dictionary is used to track the availability of rooms with room names as keys and boolean values indicating availability (True for available, False for reserved).
    
    Input/Output
    The input() function is used to receive user input for room selection and login credentials. print() is used to display messages and room statuses to the user.
    
    Functions
    Various functions, such as reserve_room() and cancel_reservation(), encapsulate logic related to room reservations, making the code modular and easier to maintain.
    
## **III. Sustainable Development Goals (SDG)**
	The CICS Room Reservation System aligns with the following Sustainable Development Goals (SDGs):
 
    SDG 9: Industry, Innovation, and Infrastructure
    The system contributes to improving infrastructure by providing a digital solution to the management of room reservations. It supports innovation in education through efficient use of resources and facilities, making room booking processes more streamlined and reducing scheduling conflicts. By digitalizing the room reservation process, the system helps optimize space utilization, reducing wasted potential of rooms that could otherwise be used for educational purposes.
    
    SDG 17: Partnerships for the Goals
    The system encourages collaboration within the educational community. By providing a shared platform for room reservations, it fosters better communication between students, faculty, and administrative staff. Additionally, the system could eventually be extended to partner with other educational institutions, allowing for resource sharing and collaborative events. This would further enhance the infrastructure and operational efficiency of educational systems, promoting collective progress toward better educational environments.

## **IV. INSTRUCTION**
    1. Login to the System
      - When the application starts, you will be prompted to enter your username and password.
      - The initial credentials for logging in are:
          Username: admin
          Password: admin
      - After successful login, you will be redirected to the main menu.
    
    2. Main Menu Options
      Once logged in, the following menu options will appear:
      - View Available Rooms: This option displays all rooms that are available for reservation. 
      - Reserve a Room: Choose this option to reserve an available room. You will be asked to input the room number for the reservation.
      - Cancel a Reservation: Use this option to cancel a reservation. You will need to provide the room number to cancel.
      - View Reserved Rooms: Displays a list of rooms that are currently reserved.
      - Exit: Choose this option to exit the system.
      
    3. Sample Menu Interaction
      - Upon selecting 1 (View Available Rooms), the system will show a list of rooms that are currently free to be booked.
      - If you select 2 (Reserve Room), you will need to input the room number you wish to book. If the room is available, it will be reserved for you.
      - If you select 3 (Cancel Reservation), you will be prompted to enter the room number for which you want to cancel the reservation.
      - Selecting 5 (Exit) will terminate the program.
