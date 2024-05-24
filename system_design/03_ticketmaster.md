
# Design a system like TicketMaster
- TicketMaster is a ticket sales and distribution company that allows users to buy tickets for events.
- 100 Million DAU

## Functional Requirements
- book tickets
- view an event
- searching for events
  
## Non-Functional Requirements
- consistency > availability (no double booking)
- strong consistency for boooking tickets
- high availability (99.99%) for searching and viewing events
- read > write
- scalability to handle surge from popular events

## Out of Scope
- GDPR compliance
- fault tolerance
- security
- backup and recovery

## Core Entities
- Event
- Location 
- Company
- Ticket

# API Design
- GET /events => [{event.title, location, company}]
- GET /events/{id} => {event.title, event.description, event.iamges, location, company, no. tickets available}
- GET /search/events?term={term}&location={location}&date={date}&type={type} => [{event}]
- POST /booking/reserve => 
  - Header: JWT sessiontoken
  - body={ticketId}
- POST /booking/confirm => 
  - Header: JWT sessiontoken
  - body={ticketId, paymentDetails}
- 