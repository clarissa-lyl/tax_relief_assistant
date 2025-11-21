ReliefGuide: An AI-Powered Assistant for Accurate and Informed Tax Relief Claims

ReliefGuide is an AI-powered FAQ chatbot designed to help Singapore taxpayers obtain clear, accurate answers to common tax relief questions. By consolidating tax relief FAQs into a structured dataset and applying Retrieval-Augmented Generation (RAG), the solution delivers fast, reliable, and easy-to-understand guidance without users needing to browse multiple IRAS webpages.

📌 Project Overview

Taxpayers in Singapore often struggle to determine:

What each relief is about

How much they can claim

Whether they qualify

What documents are required

Whether the relief is automatically granted

This is mainly because tax relief information is distributed across multiple IRAS websites, circulars, and FAQ pages. ReliefGuide addresses this challenge by centralising the information into a structured CSV and enabling intelligent conversational querying.

❗ Problem Statement

The fragmented nature of tax-relief information makes it difficult for individuals to understand eligibility criteria and claim requirements. This leads to uncertainty, incorrect claims, missed reliefs, and unnecessary queries to IRAS call centres.

Key issues faced by taxpayers:

Difficulty understanding rules and conditions

Time wasted navigating multiple webpages

Lack of a unified, user-friendly information source

High dependency on call centre and support teams

Guiding Question:
How might we create a simple, unified, AI-powered assistant that helps taxpayers quickly retrieve accurate answers to common tax relief questions using structured FAQ data?

💡 Proposed Solution

ReliefGuide is a Retrieval-Augmented Generation (RAG) chatbot that uses the uploaded CSV file as the single source of truth.

1. Consolidated Dataset (CSV)

The CSV contains:

Relief Categories

Standardised FAQ Questions

Approved Official Answers

This forms the foundational knowledge base for retrieval.

2. Intelligent Conversational Q&A

Users can ask natural-language questions such as:

“What is Earned Income Relief?”

“How do I qualify?”

“What documents are needed?”

The RAG system retrieves the closest matching FAQ from the CSV and generates an easy-to-understand, conversational reply grounded in official content.

3. High Accuracy & Maintainability

Because responses are grounded in the CSV:

No hallucinated content

Answers remain aligned with official guidance

Easy updates by simply modifying the CSV

Scalable to additional relief categories in future

🚀 Impact

ReliefGuide improves the taxpayer experience by offering:

✔ Faster Access to Information

Search time reduces from several minutes per question to seconds.

✔ Higher Confidence & Accuracy

Users receive consistent guidance based on structured, validated FAQs.

✔ Reduced Support Workload

Common, repetitive queries handled automatically.

✔ Simple Maintenance

New reliefs or clarifications can be updated by replacing or editing the CSV file.

Because it uses curated, non-sensitive data, the solution avoids misinformation and supports reliable decision-making.

🏷 Submission Tags

Capstone (Type 2)

🔒 Data Classification and Sensitivity

Official Open / Non-Sensitive

All data was openly scraped from publicly available IRAS webpages.
The dataset contains no personal data, confidential information, or restricted content.

🌐 Data Sources (Public URLs)

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/earned-income-relief

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/spouse-relief-spouse-relief-(disability)

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/foreign-domestic-worker-levy-(fdwl)-relief

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund(cpf)-relief-for-employees

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/nsman-relief-(self-wife-and-parent)                          

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/parent-relief-parent-relief-(disability)

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/grandparent-caregiver-relief

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/sibling-relief-(disability)

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/working-mother's-child-relief-(wmcr)                        

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/qualifying-child-relief-(qcr)-child-relief-(disability)

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/life-insurance-relief

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/course-fees-relief

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/special-tax-schemes/srs-contributions#title4

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-(cpf)-cash-top-up-relief

https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/compulsory-and-voluntary-medisave-contributions           
