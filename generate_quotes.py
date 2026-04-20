from fpdf import FPDF
import os

OUTPUT_DIR = "/home/ubuntu/.openclaw/workspace/projects/atelier-thamga/quotes"
LOGO_DIR = "/home/ubuntu/.openclaw/workspace/projects/atelier-thamga/logos"
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class QuotePDF(FPDF):
    def __init__(self, logo_type='photography'):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        self.add_font('DejaVu', '', f'{FONT_DIR}/DejaVuSans.ttf')
        self.add_font('DejaVu', 'B', f'{FONT_DIR}/DejaVuSans-Bold.ttf')
        self.add_font('DejaVu', 'I', f'{FONT_DIR}/DejaVuSans.ttf')
        
        self.logo_type = logo_type
        
        # Colors
        self.CREAM = (252, 248, 240)
        self.INDIGO = (30, 60, 114)
        self.TERRACOTTA = (186, 85, 54)
        self.DARK = (44, 44, 44)
        self.GRAY = (120, 120, 120)
        self.LIGHT_GRAY = (230, 230, 230)
        self.LIGHT_CREAM = (248, 244, 236)
    
    def header(self):
        # Top accent bar
        self.set_fill_color(*self.INDIGO)
        self.rect(0, 0, 210, 4, 'F')
        
        if self.logo_type == 'photography':
            # ZS Photography logo (left)
            logo_path = os.path.join(LOGO_DIR, 'zs-photography.jpg')
            if os.path.exists(logo_path):
                self.image(logo_path, x=10, y=10, w=35)
                # Title next to logo
                self.set_xy(50, 14)
                self.set_font('DejaVu', 'B', 18)
                self.set_text_color(*self.INDIGO)
                self.cell(80, 8, 'Fotograf Cekim Teklifi')
                
                # Subtitle
                self.set_xy(50, 24)
                self.set_font('DejaVu', '', 9)
                self.set_text_color(*self.GRAY)
                self.cell(80, 5, 'Zeynep Semiz | ZS Photography')
                
                # Contact info (right)
                self.set_xy(120, 14)
                self.set_font('DejaVu', '', 8)
                self.set_text_color(*self.GRAY)
                self.cell(80, 5, 'zeynepsemiz@gmail.com', align='R')
                self.ln(5)
                self.set_x(120)
                self.cell(80, 5, '@zeynepsemiz_photography', align='R')
                self.ln(5)
                self.set_x(120)
                self.cell(80, 5, '\u0130stanbul, T\u00fcrkiye', align='R')
        
        elif self.logo_type == 'atelier':
            # Atelier Thamga logo (left)
            logo_path = os.path.join(LOGO_DIR, 'atelier-thamga.jpg')
            if os.path.exists(logo_path):
                self.image(logo_path, x=10, y=8, w=40)
                # Title next to logo
                self.set_xy(55, 12)
                self.set_font('DejaVu', 'B', 20)
                self.set_text_color(*self.INDIGO)
                self.cell(80, 8, 'Atelier Thamga')
                
                # Subtitle
                self.set_xy(55, 22)
                self.set_font('DejaVu', '', 9)
                self.set_text_color(*self.GRAY)
                self.cell(80, 5, 'Zeynep Semiz | Fotograf Sanatcisi')
                
                # Contact info (right)
                self.set_xy(130, 14)
                self.set_font('DejaVu', '', 8)
                self.set_text_color(*self.GRAY)
                self.cell(70, 5, 'atelierthamga@gmail.com', align='R')
                self.ln(5)
                self.set_x(130)
                self.cell(70, 5, '@atelierthamga', align='R')
                self.ln(5)
                self.set_x(130)
                self.cell(70, 5, '\u0130stanbul, T\u00fcrkiye', align='R')
        
        elif self.logo_type == 'both':
            # Both logos - ZS Photography left, Atelier Thamga right
            zs_logo = os.path.join(LOGO_DIR, 'zs-photography.jpg')
            at_logo = os.path.join(LOGO_DIR, 'atelier-thamga.jpg')
            
            if os.path.exists(zs_logo):
                self.image(zs_logo, x=8, y=10, w=30)
            
            if os.path.exists(at_logo):
                self.image(at_logo, x=170, y=8, w=32)
            
            # Center title
            self.set_xy(40, 14)
            self.set_font('DejaVu', 'B', 16)
            self.set_text_color(*self.INDIGO)
            self.cell(130, 8, 'Fotograf Cekim Teklifi', align='C')
            
            # Subtitle
            self.set_xy(40, 23)
            self.set_font('DejaVu', '', 8)
            self.set_text_color(*self.GRAY)
            self.cell(130, 5, 'Zeynep Semiz | ZS Photography x Atelier Thamga', align='C')
            
            # Contact info (bottom center)
            self.set_xy(40, 29)
            self.set_font('DejaVu', '', 7)
            self.set_text_color(*self.GRAY)
            self.cell(130, 4, 'zeynepsemiz@gmail.com  |  @zeynepsemiz_photography  |  @atelierthamga', align='C')
        
        # Separator
        self.set_draw_color(*self.LIGHT_GRAY)
        self.set_line_width(0.3)
        self.line(15, 38, 195, 38)
        
        # Accent line
        self.set_draw_color(*self.TERRACOTTA)
        self.set_line_width(1.2)
        self.line(15, 40, 55, 40)
        
        self.ln(15)
    
    def footer(self):
        self.set_y(-22)
        self.set_draw_color(*self.LIGHT_GRAY)
        self.set_line_width(0.3)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(4)
        
        self.set_font('DejaVu', 'I', 7)
        self.set_text_color(*self.GRAY)
        self.cell(0, 4, 'ZS Photography  |  Atelier Thamga  |  @zeynepsemiz_photography  |  @atelierthamga', align='C')
        self.ln(5)
        self.cell(0, 4, 'Her paket profesyonel cekim, retouch ve online galeri icerir.', align='C')
    
    def section_title(self, title):
        self.set_font('DejaVu', 'B', 14)
        self.set_text_color(*self.INDIGO)
        self.cell(0, 10, title)
        self.ln(9)
        
        self.set_draw_color(*self.TERRACOTTA)
        self.set_line_width(0.8)
        self.line(self.get_x(), self.get_y(), self.get_x() + 45, self.get_y())
        self.ln(6)
    
    def package_box(self, name, duration, details, price, is_featured=False):
        x = self.get_x()
        start_y = self.get_y()
        
        if is_featured:
            self.set_fill_color(*self.INDIGO)
            self.set_draw_color(*self.INDIGO)
        else:
            self.set_fill_color(*self.CREAM)
            self.set_draw_color(*self.LIGHT_GRAY)
        
        # Calculate height
        line_h = 5.5
        total_lines = 1 + 1 + len(details) + 1 + 1  # name + duration + details + spacer + price
        box_h = total_lines * line_h + 14
        
        # Check page break
        if self.get_y() + box_h > 265:
            self.add_page()
            start_y = self.get_y()
        
        # Draw box
        self.rect(15, start_y, 180, box_h, 'DF')
        
        # Package name
        cy = start_y + 6
        if is_featured:
            self.set_text_color(255, 255, 255)
        else:
            self.set_text_color(*self.INDIGO)
        self.set_font('DejaVu', 'B', 12)
        self.set_xy(22, cy)
        self.cell(160, line_h, name)
        
        # Duration
        cy += line_h + 2
        if is_featured:
            self.set_text_color(180, 200, 230)
        else:
            self.set_text_color(*self.GRAY)
        self.set_font('DejaVu', '', 8)
        self.set_xy(22, cy)
        self.cell(160, line_h, f'Sure: {duration}')
        
        # Details
        cy += line_h + 2
        for detail in details:
            if is_featured:
                self.set_text_color(200, 215, 240)
            else:
                self.set_text_color(*self.DARK)
            self.set_font('DejaVu', '', 8)
            self.set_xy(22, cy)
            self.cell(160, line_h, f'\u2022  {detail}')
            cy += line_h
        
        # Price
        cy += 3
        self.set_font('DejaVu', 'B', 18)
        self.set_text_color(*self.TERRACOTTA)
        self.set_xy(22, cy)
        self.cell(160, line_h + 2, f'{price} TL')
        
        self.set_y(start_y + box_h + 4)
    
    def include_section(self, items):
        self.set_font('DejaVu', '', 9)
        self.set_text_color(*self.DARK)
        for item in items:
            self.set_x(20)
            self.cell(6, 6, '\u2022')
            self.cell(0, 6, f' {item}')
            self.ln(6)
        self.ln(2)
    
    def terms_section(self):
        self.ln(3)
        self.set_font('DejaVu', 'B', 10)
        self.set_text_color(*self.INDIGO)
        self.cell(0, 8, 'Sartlar ve Kosullar')
        self.ln(9)
        
        self.set_draw_color(*self.TERRACOTTA)
        self.set_line_width(0.5)
        self.line(self.get_x(), self.get_y(), self.get_x() + 35, self.get_y())
        self.ln(5)
        
        terms = [
            'Rezervasyon icin %30 depozito gerekmektedir.',
            'Cekim tarihinden 48 saat once ucretsiz iptal/erteleme yapilabilir.',
            'Cekim sonrasi 7-14 is gunu icinde online galeri teslim edilir.',
            'Dijital fotograflar yuksek cozunurlukte, baskiya hazir formatta teslim edilir.',
            'Ekstra retouch istekleri saatlik 250 TL ucretlendirilir.',
            'Dis mekan cekimler icin +1.500 TL lokasyon ucreti eklenir.',
            'Tekrar planlama 1 kez ucretsizdir.'
        ]
        
        self.set_font('DejaVu', '', 8)
        self.set_text_color(*self.GRAY)
        for term in terms:
            self.set_x(20)
            self.cell(6, 5, '-')
            self.multi_cell(170, 5, f' {term}')
            self.ln(1)
    
    def signature_section(self):
        self.ln(8)
        self.set_font('DejaVu', '', 9)
        self.set_text_color(*self.DARK)
        self.cell(0, 6, 'Teklifi kabul ediyorum:')
        self.ln(16)
        
        self.set_draw_color(*self.LIGHT_GRAY)
        self.set_line_width(0.3)
        self.line(15, self.get_y(), 90, self.get_y())
        self.set_x(15)
        self.set_font('DejaVu', 'I', 7)
        self.set_text_color(*self.GRAY)
        self.cell(75, 4, 'Ad Soyad / Imza')
        self.ln(10)
        
        self.set_x(15)
        self.set_draw_color(*self.LIGHT_GRAY)
        self.line(15, self.get_y(), 90, self.get_y())
        self.set_x(15)
        self.set_font('DejaVu', 'I', 7)
        self.cell(75, 4, 'Tarih')
        self.ln(14)
        
        self.set_font('DejaVu', 'B', 10)
        self.set_text_color(*self.INDIGO)
        self.cell(0, 6, 'Zeynep Semiz')
        self.ln(6)
        self.set_font('DejaVu', '', 8)
        self.set_text_color(*self.GRAY)
        self.cell(0, 4, 'ZS Photography | Atelier Thamga')


def create_baby_quote():
    pdf = QuotePDF(logo_type='both')
    pdf.add_page()
    
    pdf.set_font('DejaVu', 'B', 16)
    pdf.set_text_color(*pdf.INDIGO)
    pdf.cell(0, 10, 'Bebek & Yenidogan Cekim Teklifi')
    pdf.ln(12)
    
    pdf.set_font('DejaVu', 'I', 9)
    pdf.set_text_color(*pdf.GRAY)
    pdf.multi_cell(0, 5, 'Hayatinizin en degerli anlarini, profesyonel ve guvenli bir ortamda olumsuzlestiriyoruz. Her cekim, beginiz ve aileniz icin ozel olarak tasarlanir.')
    pdf.ln(5)
    
    pdf.section_title('Paketler')
    
    pdf.package_box(
        'Newborn (Yenidogan)',
        '1 - 1.5 saat',
        [
            '0-14 gunluk bebekler icin',
            'Swaddle, aksesuarlar dahil',
            'Aile portresi dahil',
            '25+ dijital fotograf (retouch)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '6.000'
    )
    
    pdf.package_box(
        'Baby (Bebek)',
        '45 dakika',
        [
            '3-12 aylik bebekler icin',
            'Milestone cekimi',
            '2 farkli arka plan',
            '15 dijital fotograf (retouch)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '4.000'
    )
    
    pdf.package_box(
        'Cake Smash (1 Yas)',
        '45 dakika',
        [
            '1. yas dogum gunu ozel cekim',
            'Pasta ve dekorasyon dahil',
            'Aile portresi dahil',
            '15 dijital fotograf (retouch)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '4.500',
        is_featured=True
    )
    
    pdf.ln(3)
    pdf.section_title('Tum Paketlere Dahil')
    pdf.include_section([
        'Profesyonel studyo cekimi',
        'Isik ve arka plan duzenlemesi',
        'Profesyonel retouch / light editing',
        'Online galeri (2 hafta erisim)',
        'Dijital dosyalar (yuksek cozunurluk, baskiya hazir)',
        'Cekim oncesi hazirlik rehberi'
    ])
    
    pdf.ln(2)
    pdf.section_title('Ek Hizmetler')
    
    pdf.set_font('DejaVu', '', 9)
    pdf.set_text_color(*pdf.DARK)
    addons = [
        ('Ekstra dijital fotograf', '250 TL / adet'),
        ('Baski (A4)', '200 TL'),
        ('Cerceveli baski (20x30 cm)', '450 TL'),
        ('Fotograf albumu (20 sayfa)', '800 - 1.500 TL'),
        ('Dis mekan cekim', '+1.500 TL'),
        ('Makyaj & sac', '+800 TL'),
        ('Kiyafet kiralama', '+300 TL'),
    ]
    
    for name, price in addons:
        pdf.set_x(20)
        pdf.cell(120, 6, name)
        pdf.cell(50, 6, price, align='R')
        pdf.ln(6)
    
    pdf.terms_section()
    pdf.signature_section()
    
    filepath = os.path.join(OUTPUT_DIR, 'AtelierThamga_Bebek_Yenidogan_Teklif.pdf')
    pdf.output(filepath)
    print(f'Created: {filepath}')


def create_family_quote():
    pdf = QuotePDF(logo_type='both')
    pdf.add_page()
    
    pdf.set_font('DejaVu', 'B', 16)
    pdf.set_text_color(*pdf.INDIGO)
    pdf.cell(0, 10, 'Aile Cekim Teklifi')
    pdf.ln(12)
    
    pdf.set_font('DejaVu', 'I', 9)
    pdf.set_text_color(*pdf.GRAY)
    pdf.multi_cell(0, 5, 'Ailenizin bir arada oldugu ozel anlari, dogal ve samimi bir cekimle olumsuzlestiriyoruz. Studyo veya dis mekan secenegi ile hizmetinizdeyiz.')
    pdf.ln(5)
    
    pdf.section_title('Paketler')
    
    pdf.package_box(
        'Mini Aile',
        '20 dakika',
        [
            'Tek arka plan / lokasyon',
            '5 dijital fotograf (retouch)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '3.000'
    )
    
    pdf.package_box(
        'Standart Aile (En Populer)',
        '1 saat',
        [
            '2 farkli arka plan / lokasyon',
            'Kiyafet degisimi',
            '15 dijital fotograf (retouch)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '6.000',
        is_featured=True
    )
    
    pdf.package_box(
        'Premium Aile',
        '1.5 saat',
        [
            '3 farkli arka plan / lokasyon',
            'Kiyafet degisimi',
            '30 dijital fotograf (retouch)',
            'Baski album (20 sayfa)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '10.000'
    )
    
    pdf.package_box(
        'Buyuk Aile (8+ kisi)',
        '1 saat',
        [
            'Genis aile grup cekimi',
            'Grup + tek tek portreler',
            '20 dijital fotograf (retouch)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '8.000'
    )
    
    pdf.ln(3)
    pdf.section_title('Tum Paketlere Dahil')
    pdf.include_section([
        'Profesyonel studyo cekimi',
        'Isik ve arka plan duzenlemesi',
        'Profesyonel retouch / light editing',
        'Online galeri (2 hafta erisim)',
        'Dijital dosyalar (yuksek cozunurluk, baskiya hazir)',
        'Cekim oncesi hazirlik rehberi'
    ])
    
    pdf.ln(2)
    pdf.section_title('Ek Hizmetler')
    
    pdf.set_font('DejaVu', '', 9)
    pdf.set_text_color(*pdf.DARK)
    addons = [
        ('Ekstra dijital fotograf', '250 TL / adet'),
        ('Baski (A4)', '200 TL'),
        ('Cerceveli baski (20x30 cm)', '450 TL'),
        ('Fotograf albumu (20 sayfa)', '800 - 1.500 TL'),
        ('Dis mekan cekim', '+1.500 TL'),
        ('Makyaj & sac', '+800 TL'),
        ('Kiyafet kiralama', '+300 TL'),
    ]
    
    for name, price in addons:
        pdf.set_x(20)
        pdf.cell(120, 6, name)
        pdf.cell(50, 6, price, align='R')
        pdf.ln(6)
    
    pdf.terms_section()
    pdf.signature_section()
    
    filepath = os.path.join(OUTPUT_DIR, 'AtelierThamga_Aile_Teklif.pdf')
    pdf.output(filepath)
    print(f'Created: {filepath}')


def create_children_quote():
    pdf = QuotePDF(logo_type='both')
    pdf.add_page()
    
    pdf.set_font('DejaVu', 'B', 16)
    pdf.set_text_color(*pdf.INDIGO)
    pdf.cell(0, 10, 'Cocuk Portre Cekim Teklifi')
    pdf.ln(12)
    
    pdf.set_font('DejaVu', 'I', 9)
    pdf.set_text_color(*pdf.GRAY)
    pdf.multi_cell(0, 5, 'Cocuklarinizin dogal guzelligini, eglenceli ve rahat bir cekimle olumsuzlestiriyoruz. Her yas grubuna ozel yaklasim ile unutulmaz kareler yakaliyoruz.')
    pdf.ln(5)
    
    pdf.section_title('Paketler')
    
    pdf.package_box(
        'Cocuk Mini',
        '20 dakika',
        [
            'Tek poz / arka plan',
            '5 dijital fotograf (retouch)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '2.500'
    )
    
    pdf.package_box(
        'Cocuk Standart (En Populer)',
        '45 dakika',
        [
            '2 farkli arka plan',
            'Oyuncak ve aksesuarlar dahil',
            '12 dijital fotograf (retouch)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '4.500',
        is_featured=True
    )
    
    pdf.package_box(
        'Cocuk Premium',
        '1 saat',
        [
            '3 farkli arka plan',
            'Oyuncak ve aksesuarlar dahil',
            '20 dijital fotograf (retouch)',
            'Baski (A4, 3 adet)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '7.000'
    )
    
    pdf.ln(3)
    pdf.section_title('Tum Paketlere Dahil')
    pdf.include_section([
        'Profesyonel studyo cekimi',
        'Cocuk dostu yaklasim (sakin ve eglenceli)',
        'Isik ve arka plan duzenlemesi',
        'Profesyonel retouch / light editing',
        'Online galeri (2 hafta erisim)',
        'Dijital dosyalar (yuksek cozunurluk, baskiya hazir)',
        'Cekim oncesi hazirlik rehberi'
    ])
    
    pdf.ln(2)
    pdf.section_title('Ek Hizmetler')
    
    pdf.set_font('DejaVu', '', 9)
    pdf.set_text_color(*pdf.DARK)
    addons = [
        ('Ekstra dijital fotograf', '250 TL / adet'),
        ('Baski (A4)', '200 TL'),
        ('Cerceveli baski (20x30 cm)', '450 TL'),
        ('Fotograf albumu (20 sayfa)', '800 - 1.500 TL'),
        ('Dis mekan cekim', '+1.500 TL'),
        ('Makyaj & sac', '+800 TL'),
        ('Kiyafet kiralama', '+300 TL'),
    ]
    
    for name, price in addons:
        pdf.set_x(20)
        pdf.cell(120, 6, name)
        pdf.cell(50, 6, price, align='R')
        pdf.ln(6)
    
    pdf.terms_section()
    pdf.signature_section()
    
    filepath = os.path.join(OUTPUT_DIR, 'AtelierThamga_Cocuk_Teklif.pdf')
    pdf.output(filepath)
    print(f'Created: {filepath}')


def create_portrait_quote():
    pdf = QuotePDF(logo_type='both')
    pdf.add_page()
    
    pdf.set_font('DejaVu', 'B', 16)
    pdf.set_text_color(*pdf.INDIGO)
    pdf.cell(0, 10, 'Portre Cekim Teklifi')
    pdf.ln(12)
    
    pdf.set_font('DejaVu', 'I', 9)
    pdf.set_text_color(*pdf.GRAY)
    pdf.multi_cell(0, 5, 'Kisisel, kurumsal veya sanatsal portre cekimleri. Ozelliginizi yansitan, dogal ve etkileyici kareler yakaliyoruz.')
    pdf.ln(5)
    
    pdf.section_title('Paketler')
    
    pdf.package_box(
        'Mini Portre',
        '20 dakika',
        [
            'Tek arka plan / poz',
            '3 dijital fotograf (retouch)',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '2.000'
    )
    
    pdf.package_box(
        'Standart Portre (En Populer)',
        '45 dakika',
        [
            '2 farkli arka plan',
            'Kiyafet degisimi',
            '10 dijital fotograf (retouch)',
            'LinkedIn / Sosyal medya optimizasyonu',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '4.000',
        is_featured=True
    )
    
    pdf.package_box(
        'Premium Portre',
        '1 saat',
        [
            '3 farkli arka plan',
            'Kiyafet degisimi',
            '20 dijital fotograf (retouch)',
            'Baski (A4, 3 adet)',
            'LinkedIn / Sosyal medya optimizasyonu',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '6.500'
    )
    
    pdf.package_box(
        'Kurumsal Headshot',
        '30 dakika',
        [
            'Profesyonel is portresi',
            'Tek arka plan (beyaz/gri/renkli)',
            '5 dijital fotograf (retouch)',
            'LinkedIn optimizasyonu',
            'Online galeri erisimi',
            '7-14 is gunu teslimat'
        ],
        '3.000'
    )
    
    pdf.ln(3)
    pdf.section_title('Tum Paketlere Dahil')
    pdf.include_section([
        'Profesyonel studyo cekimi',
        'Isik ve arka plan duzenlemesi',
        'Profesyonel retouch / light editing',
        'Online galeri (2 hafta erisim)',
        'Dijital dosyalar (yuksek cozunurluk, baskiya hazir)',
        'Cekim oncesi hazirlik rehberi'
    ])
    
    pdf.ln(2)
    pdf.section_title('Ek Hizmetler')
    
    pdf.set_font('DejaVu', '', 9)
    pdf.set_text_color(*pdf.DARK)
    addons = [
        ('Ekstra dijital fotograf', '250 TL / adet'),
        ('Baski (A4)', '200 TL'),
        ('Cerceveli baski (20x30 cm)', '450 TL'),
        ('Dis mekan cekim', '+1.500 TL'),
        ('Makyaj & sac', '+800 TL'),
        ('Kiyafet kiralama', '+300 TL'),
    ]
    
    for name, price in addons:
        pdf.set_x(20)
        pdf.cell(120, 6, name)
        pdf.cell(50, 6, price, align='R')
        pdf.ln(6)
    
    pdf.terms_section()
    pdf.signature_section()
    
    filepath = os.path.join(OUTPUT_DIR, 'AtelierThamga_Portre_Teklif.pdf')
    pdf.output(filepath)
    print(f'Created: {filepath}')


create_baby_quote()
create_family_quote()
create_children_quote()
create_portrait_quote()
print('\nAll PDFs with logos generated successfully!')
