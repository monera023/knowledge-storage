import './globals.css'
import { GoogleAnalytics } from "../components/GoogleAnalytics";

export const metadata = {
  metadataBase: new URL('http://www.knowledge.sto'),
  title: 'knowledge store',
  description: 'Stream of things that I devour',
  openGraph: {
    type: 'website',
    url: 'http://www.knowledge.sto',
    site_name: 'knowledge store',
    images: [
      {
        url: 'http://www.knowledge.sto/thumbnail.jpeg',
        alt: 'knowledge store homepage',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    site: 'sj',
    title: 'knowledge store',
    description: 'Stream of things that I devour',
    image: 'http://www.knowledge.sto/thumbnail.jpeg'
  }
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <link rel="icon" href="/favicon.ico" sizes="any" />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:creator" content="@monera" />
      <body>
        {/*<GoogleAnalytics />*/}
        {children}
      </body>
    </html>
  )
}
