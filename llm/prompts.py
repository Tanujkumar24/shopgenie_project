from langchain_core.prompts import PromptTemplate

comparison_prompt = PromptTemplate.from_template("""
Compare the following mobile products based on their specs, reviews, and ratings.
Return JSON that matches the ProductComparison schema.

Products:
{products_info}

Make sure to include:
- Specs: Processor, Battery, Camera, Display, Storage
- Ratings: Overall, Battery Life, Performance, Display, Camera
- Review Summary
- Best product with justification
""")