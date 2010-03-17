#!/opt/local/bin/perl -s

use Image::Magick;
use Data::Dumper;
$Data::Dumper::Terse = 1;  # avoids $VAR1 = * ; in dumper output
$Data::Dumper::Indent = $verbose? 1 : 0;  # more concise output

$photolist = shift;
$dirname = shift;
die "sample_chucks_flickr_images.pl <photolist_file> [dirname]\n" if !$photolist;

$dirname = $photolist if !$dirname;
$dirname =~ s/\.ph// if $dirname =~ /\.ph$/;
$photolist .= '.ph' if !($photolist =~ /\./);

require "$photolist";

$n = scalar(@photos);  # count photos
print "$n photos in file\n";

@sampledPhotos = ();

$nbrSampled = 0;

$firstPhoto = $photos[0];
$suffix = '_t' if !$suffix;

foreach $photo (@photos)
{
  my ($owner, $secret, $server) = ($photo->{owner},$photo->{secret},$photo->{server});
  $fnam = "$dirname/$photo->{id}$suffix.jpg";

  my $image = Image::Magick->new;
  $err = $image->Read($fnam);
  if ("$err") {
    warn "$err";
    next;
  }
  ($w,$h) = $image->Get('width','height');
  $x = $image->Resize(geometry=>'1x1');

  ($r,$g,$b) = $image->GetPixels(x=>0,y=>0,width=>1,height=>1,normalize=>1);
  $l = 0.3086*$r + 0.6094*$g + 0.0820*$b; # Haeberli Luminence equation
  undef $image;

  ($photo->{r},$photo->{g},$photo->{b},$photo->{l}) = ($r,$g,$b,$l);

  ++$nbrSampled;
  print "$nbrSampled...\n" if $nbrSampled % 50 == 0;
}

$ofname = "$dirname/samples.ph";

open (OFILE, ">$ofname");
print OFILE "\@photos = (\n";
$n = 0;
foreach $photo (@photos)
{
  print OFILE ($n++? ",\n" : "") . Dumper($photo);
}
print OFILE "\n);\n1;\n";
close OFILE;

print "$nbrSampled sampled to $ofname\n";
