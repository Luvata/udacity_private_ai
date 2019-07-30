# Introducing Local and Global Differential Privacy

**Adding random noise** to database and to the queries in order to protect people'privacy

## Definitions
### 1. Local Differential Privacy
Add noise to function data points (function inputs)
- Add noise for each individual data before inserting to database
- Users don't have to trust database owner

### 2. Global Differential Privacy
Add noise to function outputs (to the queries)
- The database contains all the private information
- Noise is added only to the **interface to the data**
- Require **Trustworthy** database owners

### 3. Trusted Curator
An owner of a database upon which Global Differential privacy is applied. They are trusted to apply DP correctly

