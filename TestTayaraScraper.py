import unittest
import os
from TayaraScraper import TayaraScraper

class TestTayaraScraper(unittest.TestCase):
    def setUp(self):
        # Initialize the TayaraScraper
        self.scraper = TayaraScraper()

    def test_scrape_links(self):
        # Test if links can be scraped without errors
        self.scraper.scrape_links()
        self.assertGreater(len(self.scraper.links), 0, "No links were scraped.")

    def test_scrape_cars(self):
        # Test if cars can be scraped without errors
        # Assume scrape_links method has been tested separately
        self.scraper.scrape_links()
        self.scraper.scrape_cars()
        self.assertGreater(len(self.scraper.cars), 0, "No cars were scraped.")

    def test_export_to_csv(self):
        # Test if CSV export can be done without errors
        # Assume scrape_links and scrape_cars methods have been tested separately
        self.scraper.scrape_links()
        self.scraper.scrape_cars()

        csv_path = "test_export.csv"
        self.scraper.export_to_csv(csv_path)
        self.assertTrue(os.path.exists(csv_path), "CSV file not created.")

        # Clean up: remove the created CSV file
        os.remove(csv_path)

if __name__ == '__main__':
    unittest.main()
