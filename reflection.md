# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design is that it included Owner, Pet, and Task, with a simple Scheduler class to create daily schedules.  
  1. User can add a pet to the system.
  2. User can create and amange care tasks such as feeding and walking. 
  3. User can generate and see a daily schedule of tasks based on priority and time. 

I included the Owner, Pet, Task, and Scheduler class. The Owner class had the responsibility of managing multiple pets and their tasks. The Pet class had the responsibility of storing pet-specific tasks and attributes. The Task class had the responsibility of representing individual care actions such as feeding or walking with attributes such as duration or priority. The scheduler class had the responsibility of sorting and filtering tasks, detecting conflicts, and handling repetitive tasks. 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

I added a pet_name tracker in Task objects so that the scheduler can filter tasks by pet. In addition, I also added a repetitive task handler logic directly in the Task class so that instead of handling it outside, it can just simplify scheduling and not have the same logic twice. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers task priority (high, medium, low), duration, due time, and reccurence. I also prioritized priority and time conflicts first because they had a greater impact on the pet owner's daily schedule.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff the scheduler makes is that conflict detection only checks for the exact time matches, not any times that overlap. This tradeoff is reasonable for this scenario because most pet tasks are short and they dont overlap, and so through checking exact times, it simplifies the code and helps avoid complexity and repetitiveness. 

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used Copilot to generate algorithms, methods, create test cases, and suggest different ways to sort, filter, and handle recurring tasks. I used prompts where I asked Copilot to write me a method to detect task conflicts without crashing the prorgram completely, or generating test cases for repetitive tasks daily. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I rejected AI suggestions that were more dependent on complex one line code snippets, even if they were more efficient and short. I verified AI suggestions by creating my test cases manually in test_pawpal.py and making sure that all my edge cases also passed.  

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested behaviors such as: 
1. Sorting tasks by priority 
2. Filtering the tasks by completion status and pet name
3. Creating repetitive tasks for daily and weekly tasks
4. Conflict detection when two tasks and their timings would clash
5. Testing pets without any tasks

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

My confidence level that my scheduler works correctly is 4/5. The scheduler works correctly for all the standard and edge cases that I have tested so far. If I had more time, I would also test for overlapping times and simultanerous multi-pet tasks. 

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I was most satisfied with being able to successfully implement repetitive tasks and the conflict detection all while keeping the code readable. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would add overlapping time conflict detection for tasks that have different and overlapping durations. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned from designing systems or working with AI on this project is that working with AI requires human oversight as well. AI helps in development but the ultimate decisions and readability is determined by the developer itself. Being the lead architect means guiding the AI suggestions while also maintaining a clear system where the ultimate decision is not taken by the artificial intelligence model. 